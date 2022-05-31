import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import streamlit as st

df = pd.read_csv('data/anime_list.csv')
df = df.copy().drop(columns = ['duration','airing','aired','background','premiered','licensors','producers','status','type'], axis = 1)

def run_data() :
    
    my_order = ['전체 데이터 보기', '기본 통계자료 보기']   

    status = st.sidebar.radio('자료 선택', my_order)  # 라디오 버튼은 1과 0이 아닌 들어가 있는 값을 띄게 된다.

    if status == my_order[0] :
        st.dataframe(df)
    elif status == my_order[1] :
        st.dataframe(df.describe())

    
    
    st.subheader('카테고리컬 데이터 컬럼 비주얼라이징')
# ['airing','type','status','licensors','producers','studios']
    chosen_col = st.selectbox('컬럼 선택', df.columns.to_list())

    my_order = df[chosen_col].value_counts().index

    if st.button('차트 확인하기'):
        fig1 = plt.figure()
        sns.countplot(data= df, x = df[chosen_col] , order = my_order)
        st.pyplot(fig1)