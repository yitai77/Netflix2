import streamlit as st
import common
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

tab1, tab2, tab3 = st.tabs(["Netflix", "South Korea", "United States"])
with tab1:

    st.title("Netflix Data")
    Data = common.data
    Data
with tab2:
    st.title("South Korea Data")
    Korean = common.get_ko_data()
    Korean

with tab3:
    st.title("United States Data")
    US = common.get_us_data()
    US