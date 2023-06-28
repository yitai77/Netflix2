import streamlit as st
import common
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

Korean = common.get_ko_data()

sk_year_counts = Korean['release_year'].value_counts().sort_index()

color = 'violet'

fig, ax = plt.subplots()
ax.bar(sk_year_counts.index, sk_year_counts.values, color=color)
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.set_xticks(sk_year_counts.index, sk_year_counts.index.astype(int), rotation=45)
ax.set_title('Netflix Shows in South Korea by Year')
st.pyplot(fig)


US = common.get_us_data()

us_year_counts = US['release_year'].value_counts().sort_index()

color = 'olive'



fig, ax = plt.subplots()
ax.bar(us_year_counts.index, us_year_counts.values, color=color)
ax.set_xlabel('Year')
ax.set_ylabel('Count')

start_year = US['release_year'].min()
end_year = (US['release_year'].max() // 10 * 10) + 10

xticks = range(start_year, end_year, 10)
ax.set_xticks(xticks)  # Set x-ticks at each decade
ax.set_xticklabels([f'{i}s' for i in xticks], rotation=0)

ax.set_title('Netflix Shows in US by Year')
st.pyplot(fig)