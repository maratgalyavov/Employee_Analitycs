import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from Funct import draw

st.markdown("# Main project page️")


def cleanup():
    df.dropna()
    df["Age"] = df["Age"].astype("int64")
    df["DistanceFromHome"] = df["DistanceFromHome"].astype("int64")
    df["MonthlyIncome"] = df["MonthlyIncome"].astype("int64")


df = pd.read_csv("Data/HR Employee Attrition.csv")
cleanup()
levels_sat = list(df["JobSatisfaction"].unique())

tab1, tab2, tab3 = st.tabs(["Satisfaction", "Wage", "WorkLifeBalance"])

with tab1:
    st.header("Satisfaction")
    df = df.sort_values(by=["JobSatisfaction","MonthlyIncome"])
    option = st.selectbox("profession",(list(df["JobRole"].unique())))
    tmp = df[df["JobRole"]==option]
    draw.drawbar(tmp["JobSatisfaction"],tmp["MonthlyIncome"])
    draw.drawbar(tmp["JobSatisfaction"],tmp["JobInvolvement"])




with tab2:
    st.header("Wage")
    df = df.sort_values(by=["MonthlyIncome", "JobSatisfaction"])
    option = st.selectbox("profession",(list(df["JobRole"].unique())))
    tmp = df[df["JobRole"] == option]


with tab3:
    st.header("WorkLifeBalance")
    df = df.sort_values(by=["WorkLifeBalance"])
    draw.drawbar(df["WorkLifeBalance"],df["DistanceFromHome"])

st.header("Job satisfaction by monthly salary")
number = st.slider("Salary", 1000, 20000)
draw.drawpie((df[(df["MonthlyIncome"] >= number - 500) & (df["MonthlyIncome"] <= number + 500)])[
    "JobSatisfaction"].value_counts())

clicked = st.button("BALOONS")
if clicked: st.balloons()
