import streamlit as st
import pandas as pd

st.markdown("# Stats logs️")
df = pd.read_csv("Data/HR Employee Attrition.csv")
df2 = pd.read_csv("Data/salary_data_cleaned.csv")
st.write(df.describe())
st.write(df2.describe())

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

with open("Data/Project_Galyavov.ipynb", "rb") as file:
    st.download_button(
        label="Notebook",
        data=file,
        file_name="Project_Galyavov.ipynb",
        mime="application/x-ipynb+json"
    )

st.sidebar.write("[my photography chanel](https://t.me/gmstreet)")

with open("Data/2022-12-05 23.25.08.jpg", "rb") as file:
    btn = st.sidebar.download_button(
        label="Sad reality",
        data=file,
        file_name="sad101.png",
        mime="image/png"
    )
