import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import streamlit as st

df = pd.read_csv('data/anime_list.csv')
df.drop('background', axis = 1, inplace= True)
i = df[df['rank'] == -1].index
df = df.drop(i)

def run_data() :
    
    my_order = ['전체 데이터 보기', '기본 통계자료 보기']   

    status = st.sidebar.radio('자료 선택', my_order)  # 라디오 버튼은 1과 0이 아닌 들어가 있는 값을 띄게 된다.

    if status == my_order[0] :
        st.dataframe(df)
    elif status == my_order[1] :
        st.dataframe(df.describe())

    st.subheader('제일 평점이 높은 애니메이션 TOP50')

    # TOP 50
    rank_top = df['rank'].sort_values().index
    st.dataframe(df.loc[rank_top].head(50))

    st.subheader('제일 인기가 많은 애니메이션 TOP50')
    favorite_top = df['favorites'].sort_values(ascending = False).index
    st.dataframe(df.loc[favorite_top].head(50))