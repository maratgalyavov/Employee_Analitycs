import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from Funct import draw

st.markdown("# Main project page️")


def cleanup(dft):
    dft.dropna()
    dft["Age"] = df["Age"].astype("int64")
    dft["DistanceFromHome"] = df["DistanceFromHome"].astype("int64")
    dft["MonthlyIncome"] = df["MonthlyIncome"].astype("int64")
    #переписать клинап под 3 датасета

df = pd.read_csv("Data/HR Employee Attrition.csv")
df2 = pd.read_csv("Data/salary_data_cleaned.csv")
df3 = pd.read_csv("Data/unemployment analysis.csv")
cleanup(df)
cleanup(df2)
cleanup((df3))
levels_sat = list(df["JobSatisfaction"].unique())
df = df.sort_values(by=["JobSatisfaction", "MonthlyIncome", "JobInvolvement"])
df2 = df2.sort_values(by=["age","avg_salary"])
df2 = df2[(df2["age"] > 0)&(df2["age"] < 100)]
tab1, tab2, tab3 = st.tabs(["Satisfaction", "Salary", "Unemployment"])

with tab1:
    st.header("Employee satisfaction")
    option = st.selectbox("profession", (list(df["JobRole"].unique())))
    tmp = df[df["JobRole"] == option]
    draw.drawbar(tmp["JobSatisfaction"], tmp["MonthlyIncome"], "JobSatisfaction", "MonthlyIncome")
    draw.drawbar(tmp["JobSatisfaction"], tmp["JobInvolvement"],"JobSatisfaction","JobInvolvement")

    st.header("Job satisfaction by monthly salary")
    number = st.slider("Salary", 1000, 20000)
    draw.drawpie((df[(df["MonthlyIncome"] >= number - 500) & (df["MonthlyIncome"] <= number + 500)])[
                     "JobSatisfaction"].value_counts())

with tab2:
    st.header("Wage")
    draw.drawstack(df2["age"],df2["avg_salary"],"age","avg_salary")


with tab3:
    st.header("Uneployment")
    years = list(range(1991, 2022))
    medians = []
    for i in years:
        medians.append(df3[str(i)].mean())
    draw.drawline(years, medians, "years","average % of unemployment")


st.sidebar.write("[my photography chanel](https://t.me/gmstreet)")

with open("Data/2022-12-05 23.25.08.jpg", "rb") as file:
    btn = st.sidebar.download_button(
        label="Sad reality",
        data=file,
        file_name="sad101.png",
        mime="image/png"
    )

clicked = st.button("BALOONS")
if clicked: st.balloons()
