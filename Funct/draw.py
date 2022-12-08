import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px


def drawpie(df, values):
    fig = px.pie(df, values=values, names=values)
    st.plotly_chart(fig)


def drawhist(df, values):
    fig = px.histogram(df, x=values)
    st.plotly_chart(fig)

def drawbox(df, x, y):
    fig = px.box(df, x=x, y=y)
    st.plotly_chart(fig)


def drawbar(df, x, y):
    fig = px.bar(df, x=x, y=y)
    st.plotly_chart(fig)


def drawstak(x, y, xt, yt):
    fig, ax = plt.subplots()
    plt.stackplot(x, y)
    ax.set_ylabel(yt)
    ax.set_xlabel(xt)
    st.pyplot(fig)


def drawline(df, x, y):
    fig = px.line(df, x=x, y=y)
    st.plotly_chart(fig)
