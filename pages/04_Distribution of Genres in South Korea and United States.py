import streamlit as st
import common
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data_1= common.data
st.title("Distribution of genres in South Korea and the United States")

# Tab 구성
tab1, tab2 = st.tabs(["South Korea", "United States"])

with tab1:
## 한국
    data_1 = common.data
    Korean = common.get_ko_data()
    data_1['main_genre'] = data_1['listed_in'].str.split(',').str[0]

    ko_genre_counts = Korean['listed_in'].str.split(',').explode().str.strip().value_counts()

    ko_top_10_genres = ko_genre_counts.head(10)

    #파이 차트
    fig, ax = plt.subplots()
    ax.pie(ko_top_10_genres, labels=ko_top_10_genres.index, autopct='%1.1f%%')

    ax.set_title('Netflix TOP 10 Genres in South Korea')
    st.pyplot(fig)
    ko_top_10_genres

with tab2:
    ##미국
    data_1 = common.data
    US = common.get_us_data()
    data_1['main_genre'] = data_1['listed_in'].str.split(',').str[0]

    us_genre_counts = US['listed_in'].str.split(',').explode().str.strip().value_counts()

    us_top_10_genres = us_genre_counts.head(10)

    fig, ax = plt.subplots()
    ax.pie(us_top_10_genres, labels=us_top_10_genres.index, autopct='%1.1f%%')

    ax.set_title('Netflix TOP 10 Genres in US')
    st.pyplot(fig)
    us_top_10_genres






# # Tab 구성
# tab1, tab2 = st.tabs(["South Korea", "United States"])

# 맨 앞에 있는 값만 추출하여 새로운 열에 저장
# data['main_kkkkk'] = data['listed_in'].str.split(',').str[0]
# kkkkk_counts = sk_data['listed_in'].str.split(',').explode().str.strip().value_counts()
# kkkkk_table = pd.DataFrame({'kkkkk': kkkkk_counts.index, 'Count': kkkkk_counts})
# top_10_kkkkks = kkkkk_table.head(10)
# # print(top_10_kkkkks)
# genre_counts = data['listed_in'].str.split(',').explode().str.strip().value_counts()
# genre_table = pd.DataFrame({'Genre': genre_counts.index, 'Count': genre_counts})
# top_10_genres = genre_table.head(10)
# # print(top_10_genres)
# data['main_genre'] = data['listed_in'].str.split(',').str[0]
# # data['main_genre']
# # with tab1:
# #     #sk_data_counts = sk_data['type'].value_counts()
# #     fig = plt.pie(top_10_kkkkks.Count, labels=top_10_kkkkks.index, autopct='%1.1f%%')
# #     plt.title('Netflix Shows in South Korea')
# #     plt.show()
# #     st.pyplot(fig)
# # with tab2:
# #     #usa_data_counts = usa_data['type'].value_counts()
# #     fig = plt.pie(top_10_genres.Count, labels=top_10_genres.index, autopct='%1.1f%%')
# #     plt.title('Netflix Shows in the United States')
# #     plt.show()
# #     st.pyplot(fig)