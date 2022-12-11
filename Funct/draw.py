import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import streamlit as st


def drawpie(df, values):
    fig = px.pie(df, values=values, names=values)
    st.plotly_chart(fig)


def drawhist(df, x, y, xl, yl):
    fig = px.histogram(df, x=x, y=y, labels={x: xl, y: yl}, histfunc="avg")
    fig.update_layout(bargap=0.1)
    st.plotly_chart(fig)


def drawbox(df, x, y, xl, yl):
    fig = px.box(df, x=x, y=y, labels={x: xl, y: yl})
    st.plotly_chart(fig)


def drawbar(df, x, y, xl, yl):
    fig = px.bar(df, x=x, y=y, labels={x: xl, y: yl})
    st.plotly_chart(fig)


def drawscatter(df, x, y, xl, yl):
    fig = px.scatter(df, x=x, y=y, trendline="ols", color="Rating", labels={x: xl, y[0]: yl})
    st.plotly_chart(fig)


def drawline(df, x, y, xl, yl):
    fig = px.line(df, x=x, y=y, labels={x: xl, y[0]: yl})
    st.plotly_chart(fig)


def drawheat(df, x, y, xl, yl):
    fig = px.density_heatmap(df, x=x, y=y, labels={x: xl, y: yl}, color_continuous_scale="sunsetdark", nbinsx=30,
                             nbinsy=30)
    st.plotly_chart(fig)
