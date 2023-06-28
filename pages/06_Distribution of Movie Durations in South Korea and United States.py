import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import common
import seaborn as sns


data_1 = common.data


# st.title( “Distribution of TV show season counts in South Korea and the United States” )
st.title("Distribution of Movie Durations in South Korea and the United States")




sk_data = data_1[data_1['country'] == 'South Korea']
usa_data = data_1[data_1['country'] == 'United States']

# Tab 구성
tab1, tab2, tab3 = st.tabs(["South Korea", "United States", "Comparison"])


sk_data_counts = sk_data['type'].value_counts()
usa_data_counts = usa_data['type'].value_counts()


# st.title(“South Korea-Data”)
# sk_data = data[data[‘country’] == ‘South Korea’]
# st.write(sk_data)
# st.title(“United States-Data”)
# usa_data = data[data[‘country’] == ‘United States’]
# st.write(usa_data)

with tab1:
 sk_movies_data = data_1[(data_1['country'] == 'South Korea') & (data_1['type'] == 'Movie')]


 duration = sk_movies_data['duration'].str.replace(' min', '').astype(int)
 plt.figure(figsize=(10, 6))
 sns.distplot(duration, bins=30, hist=True, kde=True, color='red')
 plt.title('Distribution of Movie Durations for Netflix Content in South Korea')
 plt.xlabel('Duration (minutes)')
 plt.ylabel('Density')
 plt.show()
 st.pyplot(plt)
 st.write("KR Duration Data")
 duration


with tab2:
 usa_movies_data = data_1[(data_1['country'] == 'United States') & (data_1['type'] == 'Movie')]
 duration = usa_movies_data['duration'].str.replace('min', '').astype(int)
 plt.figure(figsize=(10, 6))
 sns.distplot(duration, bins=30, hist=True, kde=True, color='green')
 plt.title('Distribution of Movie Durations for Netflix Content in United States')
 plt.xlabel('Duration (minutes)')
 plt.ylabel('Density')
 plt.show()
 st.pyplot(plt)
 st.write("US Duration Data")
 duration

with tab3:
 plt.figure(figsize=(10, 6))
 sk_movies_data = data_1[(data_1['country'] == 'South Korea') & (data_1['type'] == 'Movie')]
 duration_sk = sk_movies_data['duration'].str.replace(' min', '').astype(int)
 plt.hist(duration_sk, bins=30, density=True, alpha=0.5, color='red', label='South Korea')
 sns.kdeplot(duration_sk, color='red', label='South Korea')
 usa_movies_data = data_1[(data_1['country'] == 'United States') & (data_1['type'] == 'Movie')]
 duration_usa = usa_movies_data['duration'].str.replace(' min', '').astype(int)
 plt.hist(duration_usa, bins=30, density=True, alpha=0.5, color='green', label='United States')
 sns.kdeplot(duration_usa, color='green', label='United States')
 plt.title('Distribution of Movie Durations for Netflix Content')
 plt.xlabel('Duration (minutes)')
 plt.ylabel('Density')
 plt.legend()
# 그래프 출력
 plt.show()
 st.pyplot(plt)