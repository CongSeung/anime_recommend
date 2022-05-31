import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import random
import seaborn as sns
import streamlit as st

from app_data import run_data
from app_home import run_home

def main():
    
    st.title("Recommand Animation")

    menu = ['Home', 'EDA' ,'ML']

    choice = st.sidebar.selectbox('메 뉴 선 택', menu)

    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_data()



if __name__ == '__main__':
    main()