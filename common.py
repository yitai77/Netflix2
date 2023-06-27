import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv("netflix1.csv")


@st.cache_data
def get_us_data():
    usa_data = data[data['country'] == 'United States']
    return usa_data


def get_ko_data():
    sk_data = data[data['country'] == 'South Korea']
    return sk_data


def page_config():
    st.set_page_config(
        page_title="Netflix : South Korea and United States",
        page_icon="🎥",
    )