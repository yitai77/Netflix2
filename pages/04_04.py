import streamlit as st
import common
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data_1= common.data
## 한국
Korean = common.get_ko_data()
data_1['main_genre'] = data_1['listed_in'].str.split(',').str[0]

ko_genre_counts = Korean['listed_in'].str.split(',').explode().str.strip().value_counts()

ko_top_10_genres = ko_genre_counts.head(10)

#파이 차트
fig, ax = plt.subplots()
ax.pie(ko_top_10_genres, labels=ko_top_10_genres.index, autopct='%1.1f%%')

ax.set_title('Netflix Shows in South Korea')

st.pyplot(fig)


##미국

US = common.get_us_data()
data_1['main_genre'] = data_1['listed_in'].str.split(',').str[0]

us_genre_counts = US['listed_in'].str.split(',').explode().str.strip().value_counts()

us_top_10_genres = us_genre_counts.head(10)

fig, ax = plt.subplots()
ax.pie(us_top_10_genres, labels=us_top_10_genres.index, autopct='%1.1f%%')

ax.set_title('Netflix Shows in the US')

st.pyplot(fig)
