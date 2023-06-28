import streamlit as st
import common
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.title("South Korea-Data")

Korean = common.get_ko_data()
Korean

st.title("United States-Data")
US = common.get_us_data()
US