import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import random
import seaborn as sns
import streamlit as st

from app_data import run_data
from app_home import run_home
from app_recommend import run_recomm
from app_search import run_search

def main():
    
    st.title("Recommand Animation")

    menu = ['Home', 'Search' ,'Data', 'Recommend']

    choice = st.sidebar.selectbox('메 뉴 선 택', menu)

    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_search()
    elif choice == menu[2]:
        run_data()
    elif choice == menu[3]:
        run_recomm()



if __name__ == '__main__':
    main()