import pandas as pd
import streamlit as st
from Funct import draw
from Funct import tools

st.markdown("# Main project page️")

df = pd.read_csv("Data/HR Employee Attrition.csv")
df2 = pd.read_csv("Data/salary_data_cleaned.csv")
df3 = pd.read_csv("Data/unemployment analysis.csv")

df, df2, df3 = tools.cleanup(df, df2, df3)
df = tools.modify(df)
levels_sat = sorted(list(df["JobSatisfaction"].unique()))
df = df.sort_values(by=["JobSatisfaction", "MonthlyIncome", "JobInvolvement"])
df2 = df2.sort_values(by=["age", "avg_salary"])

tab1, tab2, tab3 = st.tabs(["Satisfaction", "Salary", "Unemployment"])

with tab1:
    st.header("Employee satisfaction")
    st.write(
        "I assume that monthly income and job involvement have a healthy effect on job satisfaction, to prove it, I plotted bar charts for each of these parameters in general and for different professions. Charts you see below are a great proof for my hypothesis, as they show that income has a very similar effect on one's level of satisfaction as job involvement, where individuals with highest income and/or involvement tend to be more satisfied with their career")
    option = st.selectbox("profession", (["All"] + list(df["JobRole"].unique())))
    if option == "All":
        tmp = df
    else:
        tmp = df[df["JobRole"] == option]
    draw.drawbar(tmp, "JobSatisfaction", "MonthlyIncome", "Job Satisfaction", "Monthly Income")
    draw.drawbar(tmp, "JobSatisfaction", "JobInvolvement", "Job Satisfaction", "Job Involvement")
    st.header("Job satisfaction by monthly salary")
    st.write(
        "On the pie chart below, i represented different percentages of job satisfaction based on salary, the chart is interactive so you can select desired level of income and view percentages of different satisfaction levels among individuals whose income is within +-500$ of the selected amount")
    number = st.slider("Salary", 1000, 20000)
    df = df[(df["MonthlyIncome"] >= number - 500) & (df["MonthlyIncome"] <= number + 500)]
    draw.drawpie(df, "JobSatisfaction")

with tab2:
    st.header("Wage")
    st.write("Bow chart below shows minimum and average wage requirements for individuals based on their age. Box chart was chosen here to make average values more clear as well as show extremes. I want to prove that most people get paid above their minimum threshold and this gap is not dependant on one's age")
    draw.drawbox(df2, "age", "min_salary", "Age", "Minimal Salary")
    draw.drawbox(df2, "age", "avg_salary", "Age", "Average Salary")
    st.write("We can observe that two charts are almost identical apart from wages being noticeably higher in the second one. This example shows that most workers get paid on average 40-70 thousand $ more than their minimal requirements")

with tab3:
    st.header("Unemployment")
    years = list(map(str, (range(1991, 2022))))
    medians = []
    for i in years:
        medians.append(df3[str(i)].mean())
    data = {"year": years, "mids": medians}
    df69 = pd.DataFrame.from_dict(data)
    draw.drawline(df69, "year", "mids", "Year", "Percentage Of Unemployment")

with open("Data/2022-12-05 23.25.08.jpg", "rb") as file:
    btn = st.sidebar.download_button(
        label="Sad reality",
        data=file,
        file_name="sad101.png",
        mime="image/png"
    )
st.sidebar.write("[my photography chanel](https://t.me/gmstreet)")

clicked = st.button("BALLOONS")
if clicked:
    st.balloons()
