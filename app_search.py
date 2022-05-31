import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import streamlit as st

df = pd.read_csv('data/anime_list.csv')
df.drop('background', axis = 1, inplace= True)
i = df[df['rank'] == -1].index
df = df.drop(i)


def run_search():
   
    ## 
    title_input = st.sidebar.text_input('원하는 제목 찾기')

    contain_title = df['title'].str.lower().str.contains(title_input)
    
    st.subheader('애니메이션 제목 찾기')
    if st.sidebar.button('제목 검색하기'):

        st.dataframe(df.loc[contain_title])


    ##
    st.subheader('원하는 컬럼 정렬해서 보기')
    
    sort_sel = st.sidebar.selectbox('원하는 컬럼 선택', df.columns.to_list())

    my_order_1 = ['올림차순', '내림차순']   

    my_sel_1 = st.sidebar.radio('자료 선택', my_order_1)

    if my_sel_1 == '올림차순':
        my_sel_2 = True
    else :
        my_sel_2 = False

    if st.sidebar.button('정렬한 후 확인하기'):
        favorite_top = df[sort_sel].sort_values(ascending = my_sel_2).index
        st.dataframe(df.loc[favorite_top].head(100))



        