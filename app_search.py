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
    st.subheader('제일 평점이 높은 애니메이션 TOP50')

    # TOP 50
    rank_top = df['rank'].sort_values().index
    st.dataframe(df.loc[rank_top].head(50))

    st.subheader('제일 인기가 많은 애니메이션 TOP50')
    favorite_top = df['favorites'].sort_values(ascending = False).index
    st.dataframe(df.loc[favorite_top].head(50))

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
        