import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import streamlit as st


def drawpie(df, values):
    fig = px.pie(df, values=values, names=values)
    st.plotly_chart(fig)


def drawhist(df, values):
    fig = px.histogram(df, x=values)
    st.plotly_chart(fig)


def drawbox(df, x, y, xl, yl):
    fig = px.box(df, x=x, y=y, labels={x: xl, y: yl})
    st.plotly_chart(fig)


def drawbar(df, x, y, xl, yl):
    fig = px.bar(df, x=x, y=y, labels={x: xl, y: yl})
    st.plotly_chart(fig)


# def drawstak(x, y, xt, yt):
#     fig, ax = plt.subplots()
#     plt.stackplot(x, y)
#     ax.set_ylabel(yt)
#     ax.set_xlabel(xt)
#     st.pyplot(fig)


def drawline(df, x, y, xl, yl):
    fig = px.line(df, x=x, y=y, labels={x: xl, y[0]: yl})
    st.plotly_chart(fig)
