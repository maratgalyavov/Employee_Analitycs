import streamlit as st
import pandas as pd

st.markdown("# Stats logs️")
df = pd.read_csv("Data/HR Employee Attrition.csv")
st.write(df.describe())