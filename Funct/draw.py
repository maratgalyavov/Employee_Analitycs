import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px


def drawpie(i):
    fig, ax = plt.subplots()
    i.plot.pie()
    st.pyplot(fig)

def drawbox(df):
    fig = px.box(df, x = "JobSatisfaction", y= "MonthlyIncome")
    st.plotly_chart(fig)

def drawbar(x, y, xt, yt):
    fig, ax = plt.subplots()
    plt.bar(x,y)
    ax.set_ylabel(yt)
    ax.set_xlabel(xt)
    st.pyplot(fig)


def drawstak(x, y, xt, yt):
    fig, ax = plt.subplots()
    plt.stackplot(x, y)
    ax.set_ylabel(yt)
    ax.set_xlabel(xt)
    st.pyplot(fig)

def drawline(x, y, xt, yt):
    fig, ax = plt.subplots()
    plt.plot(x, y)
    ax.set_ylabel(yt)
    ax.set_xlabel(xt)
    st.pyplot(fig)