import streamlit as st
import common
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


st.title("KOR-Data")
Korean = common.get_ko_data()


sk_data_counts = Korean['type'].value_counts()


colors = ['violet', 'mistyrose']


fig, ax = plt.subplots()
ax.pie(sk_data_counts, labels=sk_data_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'white', 'width':0.7}, colors = colors)
ax.axis('equal')
ax.set_title('Netflix Shows in the South Korea')

st.pyplot(fig)


st.title("US-Data")
US = common.get_us_data()

#색상 설정
colors = ['green', 'mistyrose']

us_data_counts = US['type'].value_counts()

fig, ax = plt.subplots()
ax.pie(us_data_counts, labels=us_data_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'white', 'width':0.7}, colors = colors)
ax.axis('equal')
ax.set_title('Netflix Shows in the US')

st.pyplot(fig)