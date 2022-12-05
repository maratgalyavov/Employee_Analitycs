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
    st.header("Employee satisfaction")
    df = df.sort_values(by=["JobSatisfaction", "MonthlyIncome"])
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


with tab3:
    st.header("WorkLifeBalance")


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
