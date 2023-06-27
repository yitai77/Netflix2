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