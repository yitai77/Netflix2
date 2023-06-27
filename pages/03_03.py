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
ax.set_xticks(sk_type_counts.index, sk_type_counts.index.astype(int), rotation=45)
ax.set_title('Netflix Shows in the South Korea by year')
st.pyplot(fig)