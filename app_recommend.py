import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import random
import seaborn as sns
import streamlit as st
import base64
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def run_recomm():
    st.subheader('애니메이션 추천해드립니다!')

    anime = pd.read_csv('data/anime_list.csv')
    anime_cleaned = anime.copy().drop(columns = ['duration','airing','aired','background','premiered','licensors','producers','status','type'], axis = 1)
    tfidfvec = TfidfVectorizer(stop_words = 'english')
    anime_cleaned['synopsis']=anime_cleaned['synopsis'].fillna('')
    tfidf_matrix = tfidfvec.fit_transform(anime_cleaned['synopsis'])
    
    cosine_sim=linear_kernel(tfidf_matrix,tfidf_matrix)

    indices = pd.Series(anime_cleaned.index,index = anime_cleaned['title']).drop_duplicates()

    st.dataframe(anime_cleaned[['title','favorites','rank','score','genres']])

    input_anime = st.sidebar.text_input('시청해본 애니메이션 입력')

    def recommender(title, cosine_sim = cosine_sim):

        #get the index based on title
        index = indices[title]
        
        #get cosine similarity for title
        cosine_sim_for_title = list(enumerate(cosine_sim[index]))

        #sort by cosine similarity
        sorted_by_second = sorted(cosine_sim_for_title, key = lambda x:x[1])
        chosen = sorted_by_second[1:6]

        anime_indices = [i[0] for i in chosen]

        return anime_cleaned.iloc[anime_indices]   

    if st.sidebar.button('추천받기'):
    
        st.dataframe(recommender(input_anime))


