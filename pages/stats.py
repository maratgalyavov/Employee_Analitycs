import streamlit as st
import pandas as pd

st.markdown("# Stats logs️")
st.write("Here you can view descriptive statistics for all my datasets as well as download them in .csv format. Also listed below is my jupyter notebook for this project")
df = pd.read_csv("Data/HR Employee Attrition.csv")
df2 = pd.read_csv("Data/salary_data_cleaned.csv")
df3 = pd.read_csv("Data/unemployment analysis.csv")
options = ['employee_anal.csv', 'salary_data.csv', 'unemployment_data.csv']
option = st.selectbox("Dataset", ['employee_anal.csv', 'salary_data.csv', 'unemployment_data.csv'], )
if options.index(option) == 0:
    st.write(df.describe())
elif options.index(option) == 1:
    st.write(df2.describe())
elif options.index(option) == 2:
    st.write(df3.describe())

col1, col2, col3 = st.columns(3)


@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')


with col1:
    st.download_button(
        label="Employee dataset as CSV",
        data=convert_df(df),
        file_name='employee_anal.csv',
        mime='text/csv',
    )
with col2:
    st.download_button(
        label="Salary dataset as CSV",
        data=convert_df(df2),
        file_name='salary_data.csv',
        mime='text/csv',
    )
with col3:
    st.download_button(
        label="Unemployed dataset as CSV",
        data=convert_df(df3),
        file_name='unemployment_data.csv',
        mime='text/csv',
    )
st.write("[Jupyter notebook](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")

with open("Data/Project_Galyavov.ipynb", "rb") as file:
    st.sidebar.download_button(
        label="Notebook",
        data=file,
        file_name="Project_Galyavov.ipynb",
        mime="application/x-ipynb+json"
    )

with open("Data/2022-12-05 23.25.08.jpg", "rb") as file:
    btn = st.sidebar.download_button(
        label="Sad reality",
        data=file,
        file_name="sad101.png",
        mime="image/png"
    )
st.sidebar.write("[my photography chanel](https://t.me/gmstreet)")
