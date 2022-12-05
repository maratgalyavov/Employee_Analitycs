import streamlit as st
import pandas as pd

st.markdown("# Stats logs️")
df = pd.read_csv("Data/HR Employee Attrition.csv")
st.write(df.describe())


@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')


csv = convert_df(df)

st.download_button(
    label="Employee dataset as CSV",
    data=csv,
    file_name='employee_anal.csv',
    mime='text/csv',
)

st.download_button(
    label="Jupyter",
    data="Data/Project_Galyavov.ipynb",
    file_name='employee_anal.csv',
    mime='text/ipynb',
)

st.sidebar.write("[my photography chanel](https://t.me/gmstreet)")

with open("Data/2022-12-05 23.25.08.jpg", "rb") as file:
    btn = st.sidebar.download_button(
        label="Sad reality",
        data=file,
        file_name="sad101.png",
        mime="image/png"
    )
