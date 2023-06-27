import streamlit as st
import common
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.title("US-Data")

st.dataframe(common.get_us_data(),
             use_container_width=True,
             hide_index=True)


st.title("KO-Data")

st.dataframe(common.get_ko_data(),
             use_container_width=True,
             hide_index=True)