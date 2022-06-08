import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import random
import seaborn as sns
import streamlit as st
import base64
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df = pd.read_csv('data/anime_list.csv')
df.drop('background', axis = 1, inplace= True)
i = df[df['rank'] == -1].index
df = df.drop(i)

anime = pd.read_csv('data/anime_list.csv')
anime_cleaned = anime.copy().drop(columns = ['duration','airing','aired','background','premiered','licensors','producers','status','type'], axis = 1)
tfidfvec = TfidfVectorizer(stop_words = 'english')
anime_cleaned['synopsis']=anime_cleaned['synopsis'].fillna('')
tfidf_matrix = tfidfvec.fit_transform(anime_cleaned['synopsis'])

cosine_sim=linear_kernel(tfidf_matrix,tfidf_matrix)

indices = pd.Series(anime_cleaned.index,index = anime_cleaned['title']).drop_duplicates()

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

def run_search():
    # 정렬의 기준이될 컬럼 선택하기
    st.sidebar.text('------------')
    sort_sel = st.sidebar.selectbox('정렬할 기준 선택', df.columns.to_list())
    st.sidebar.text('------------')

    # 정렬방식 선택할 라디오 버튼 만들기
    my_order_1 = ['올림차순', '내림차순']   

    my_sel_1 = st.sidebar.radio('정렬 방법', my_order_1)

    if my_sel_1 == '올림차순':
        my_sel_2 = True
    else :
        my_sel_2 = False
    st.sidebar.text('------------')
    

    # 제목 검색하기
    title_input = st.sidebar.text_input('원하는 제목 찾기')

    contain_title = df['title'].str.lower().str.contains(title_input)
    
    st.subheader('애니메이션 제목 찾기')
    st.text('')
    
    # 기본 데이터 프레임고 검색 결과 데이터프레임 출력하기
    with st.expander('기본 데이터 보기'):
        st.dataframe(df.sort_values(by= sort_sel ,ascending=my_sel_2))

    if st.sidebar.button('제목 검색하기'):
        st.subheader('검색 결과')
        st.dataframe(df.loc[contain_title].sort_values(by= sort_sel ,ascending=my_sel_2))

    # 애니메이션 추천하기
    input_anime = st.sidebar.text_input('추천이요! 시청한 만화 제목 입력!')

    if st.sidebar.button('추천받기'):
    
        st.dataframe(recommender(input_anime))


        