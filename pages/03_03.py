import streamlit as st
import common
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

Korean = common.get_ko_data()

sk_year_counts = Korean['release_year'].value_counts().sort_index()

color = ['violet']

fig, ax = plt.subplots()
ax.bar(sk_year_counts.index, sk_year_counts.values, color=color)
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.set_xticks(sk_year_counts.index, sk_year_counts.index.astype(int), rotation=45)
ax.set_title('Netflix Shows in the South Korea by year')
st.pyplot(fig)


US = common.get_us_data()

us_year_counts = US['release_year'].value_counts().sort_index()

color = ['olive']


start_year = us_year_counts.index.min()  # 최소 연도
end_year = us_year_counts.index.max()    # 최대 연도

xticks = np.arange(start_year, end_year+1, 10)

fig, ax = plt.subplots()
ax.bar(us_year_counts.index, us_year_counts.values, color=color)
ax.set_xlabel('Year')
ax.set_ylabel('Count')
# ax.set_xticklabels(xticks.astype(int), rotation=45)
ax.set_xticklabels(xticks.astype(int), rotation=45)  # 올바른 메서드 이름 사용
ax.set_title('Netflix Shows in the US by year')
st.pyplot(fig)



