import streamlit as st
import pandas as pd
import numpy as np
 
st.write("""
# My first app
Hello *world!*
""")

number = st.slider("Pick a number", 0, 100)
 
df = pd.read_csv("my_data.csv")
df = pd.DataFrame(np.random.randn(number))
st.line_chart(df)