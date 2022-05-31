import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import random
import seaborn as sns
import streamlit as st
import base64


def run_home():
    st.subheader('이 애니메이션은 어떠세요?')
    st.subheader('재밌어요!')

    # ### gif 파일 넣기
    # """### gif from local file"""
    # file_ = open("data/streamlit-app-2022-05-27-17-05-37 (3).gif", "rb")
    # contents = file_.read()
    # data_url = base64.b64encode(contents).decode("utf-8")
    # file_.close()

    # st.markdown(
    #     f'<img src="data:image/gif;base64,{data_url}" alt="Explanation video gif">',
    #     unsafe_allow_html=True,
    # )


    #### 영상넣기
    # st.text('영상 예시')
    # video_file = open('data/streamlit-app-2022-05-27-15-05-59.webm', 'rb')
    # st.video(video_file)
        
