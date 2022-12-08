import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from Funct import draw

st.markdown("# Main project page️")

df = pd.read_csv("Data/HR Employee Attrition.csv")
df2 = pd.read_csv("Data/salary_data_cleaned.csv")
df3 = pd.read_csv("Data/unemployment analysis.csv")


def cleanup(df01, df02, df03):
    df01.dropna()
    df02.dropna()
    df03.dropna()
    df["Age"] = df["Age"].astype("int64")
    df["DistanceFromHome"] = df["DistanceFromHome"].astype("int64")
    df["MonthlyIncome"] = df["MonthlyIncome"].astype("int64")
    df02 = df02[(df02["age"] > 0) & (df02["age"] < 100)]
    return df01, df02, df03

def modify(df0):
    return df0.assign(increase=lambda x: x.MonthlyIncome * x.PercentSalaryHike * 0.01)

df, df2, df3 = cleanup(df, df2, df3)
levels_sat = sorted(list(df["JobSatisfaction"].unique()))
df = df.sort_values(by=["JobSatisfaction", "MonthlyIncome", "JobInvolvement"])
df2 = df2.sort_values(by=["age", "avg_salary"])


tab1, tab2, tab3 = st.tabs(["Satisfaction", "Salary", "Unemployment"])

with tab1:
    st.header("Employee satisfaction")
    st.write(
        "I assume that monthly income and jib involvement have little to no effect on job satisfaction, to prove it, I plotted bar charts for each of these parameters in general and for different professions. Charts you see below are a great proof for my hyphotezis, as they show that income has no impact on satisfaction, as is job involvement")
    option = st.selectbox("profession", (["All"] + list(df["JobRole"].unique())))
    if option == "All":
        tmp = df
    else:
        tmp = df[df["JobRole"] == option]
    draw.drawbar(tmp, "JobSatisfaction","MonthlyIncome")
    draw.drawbar(tmp,"JobSatisfaction", "JobInvolvement")
    st.header("Job satisfaction by monthly salary")
    number = st.slider("Salary", 1000, 20000)
    df = df[(df["MonthlyIncome"] >= number - 500) & (df["MonthlyIncome"] <= number + 500)]
    draw.drawpie(df,"JobSatisfaction")

with tab2:
    st.header("Wage")
    ages = list(df2["age"].unique())
    avg_wag = []
    for i in ages:
        avg_wag.append((df2[df2["age"] == i])["min_salary"].mean())
    draw.drawstak(ages, avg_wag, "age", "min_salary")

with tab3:
    st.header("Uneployment")
    years = list(range(1991, 2022))
    medians = []
    for i in years:
        medians.append(df3[str(i)].mean())
    draw.drawline(years, medians, "years", "average % of unemployment")

with open("Data/2022-12-05 23.25.08.jpg", "rb") as file:
    btn = st.sidebar.download_button(
        label="Sad reality",
        data=file,
        file_name="sad101.png",
        mime="image/png"
    )
st.sidebar.write("[my photography chanel](https://t.me/gmstreet)")

clicked = st.button("BALOONS")
if clicked: st.balloons()
