import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import random
import seaborn as sns
import streamlit as st

from app_describe import run_data
from app_home import run_home
from app_search import run_search



def main():
    
    st.title("Recommend Animation")

    menu = ['Home', 'Describe','Search']

    choice = st.sidebar.selectbox('메 뉴 선 택', menu)

    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_data()
    elif choice == menu[2]:
        run_search()
    

if __name__ == '__main__':
    main()