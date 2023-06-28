import streamlit as st
import common
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


st.title("KOR-Data")
tab1, tab2, tab3 = st.tabs(["South Korea", "United States", "Comparison"])
Korean = common.get_ko_data()

with tab1:
    sk_data_counts = Korean['type'].value_counts()


    colors = ['violet', 'mistyrose']


    fig, ax = plt.subplots()
    ax.pie(sk_data_counts, labels=sk_data_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'white', 'width':0.7}, colors = colors)
    ax.axis('equal')
    ax.set_title('Netflix Shows in South Korea')

    st.pyplot(fig)
    sk_data_counts

with tab2:
    st.title("US-Data")
    US = common.get_us_data()

#색상 설정
    colors = ['green', 'mistyrose']

    us_data_counts = US['type'].value_counts()

    fig, ax = plt.subplots()
    ax.pie(us_data_counts, labels=us_data_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'white', 'width':0.7}, colors = colors)
    ax.axis('equal')
    ax.set_title('Netflix Shows in US')

    st.pyplot(fig)
    us_data_counts

with tab3:
    # 그래프 영역 설정
    fig, ax = plt.subplots()
    # South Korea 그래프 그리기
    ax.plot(sk_data_counts.index, sk_data_counts, marker='o', linestyle='-', color='violet', label='South Korea')

    # United States 그래프 그리기
    ax.plot(us_data_counts.index, us_data_counts, marker='o', linestyle='-', color='green', label='United States')

    # 축과 제목 설정
    plt.xlabel('Type')
    plt.ylabel('Count')
    plt.title('Netflix Shows Comparison')
    plt.legend()

    st.pyplot(fig)
