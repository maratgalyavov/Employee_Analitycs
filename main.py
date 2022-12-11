import pandas as pd
import streamlit as st

from Funct import draw
from Funct import tools

st.markdown("# Main page️")

df = pd.read_csv("Data/HR Employee Attrition.csv")
df2 = pd.read_csv("Data/salary_data_cleaned.csv")
df3 = pd.read_csv("Data/unemployment analysis.csv")

df, df2, df3 = tools.cleanup(df, df2, df3)
df = tools.modify(df)
df = df.sort_values(by=["JobSatisfaction", "MonthlyIncome", "JobInvolvement"])
df2 = df2.sort_values(by=["age", "avg_salary"])
tab1, tab2, tab3 = st.tabs(["Satisfaction", "Salary", "Unemployment"])

with tab1:
    st.header("Employee satisfaction")
    st.write(
        "I assume that monthly income and job involvement have a healthy effect on job satisfaction, to prove it, I plotted bar charts for each of these parameters in general and for different professions. Charts you see below are a great disproof for my hypothesis, as they show that income has a very subtle effect on one's level of satisfaction, same for job involvement, where individuals with highest income and/or involvement tend to be more satisfied with their career, but only slightly")
    st.write(
        "Bar chaart was chosen to represent this because it is easy to undersrtand and very easy to compare parameters")
    option = st.selectbox("profession", (["All"] + list(df["JobRole"].unique())))
    if option == "All":
        tmp = df
    else:
        tmp = df[df["JobRole"] == option]
    draw.drawhist(tmp, "MonthlyIncome","JobSatisfaction", "Monthly Income","Job Satisfaction")
    draw.drawhist(tmp, "JobInvolvement", "JobSatisfaction", "Job Involvement", "Job Satisfaction")
    st.header("Job satisfaction by monthly salary")
    st.write(
        "On the pie chart below, i represented different percentages of job satisfaction based on salary, the chart is interactive so you can select desired level of income and view percentages of different satisfaction levels among individuals whose income is within +-500$ of the selected amount")
    st.write("i chose pie chart here because it is the best plot to depict percentages and ratios")
    number = st.slider("Salary", 1000, 20000)
    df = df[(df["MonthlyIncome"] >= number - 500) & (df["MonthlyIncome"] <= number + 500)]
    draw.drawpie(df, "JobSatisfaction")

with tab2:
    st.header("Wage")
    st.write(
        "Box chart below shows minimum and average wage requirements for individuals based on their age. Box chart was chosen here to make average values more clear as well as show extremes. I want to prove that most people get paid above their minimum threshold and this gap is not dependant on one's age")
    st.write(
        "box charts are great to present gradial statistical data and it's deviations, while simultaniously looking cool")
    draw.drawscatter(df2, "age", "min_salary", "Age", "Minimal Salary")
    draw.drawscatter(df2, "age", "avg_salary", "Age", "Average Salary")
    st.write(
        "We can observe that two charts are almost identical apart from wages being noticeably higher in the second one. This example shows that most workers get paid on average 40-70 thousand $ more than their minimal requirements")
    draw.drawheat(df2, "age", "avg_salary", "Age", "Average Salary")

with tab3:
    st.header("Unemployment")
    st.write(
        "Level of unemployment generally reflects what is happening with the world economy. line chart below depicts unemployment percentage in europe, us and average among all countries. all three trends follow the same pattern, proving the point that level of uneployment is a great metric for analyzing worldwide economical situation ")
    st.write("")
    years = list(map(str, (range(1991, 2022))))
    medians = []
    europe = []
    us = []
    for i in years:
        medians.append(df3[str(i)].mean())
        europe.append((df3[df3["Country Code"] == "ECS"])[str(i)].mean())
        us.append((df3[df3["Country Code"] == "GBR"])[str(i)].mean())
    data = {"year": years, "mids": medians, "europe": europe, "us": us}
    df69 = pd.DataFrame.from_dict(data)
    ys = ["mids", "europe", "us"]
    draw.drawline(df69, "year", ys, "Year", "Percentage Of Unemployment")
    draw.drawbar(df69, "year", ys, "Year", "Percentage Of Unemployment")

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
