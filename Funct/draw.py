import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def drawpie(i):
    fig, ax = plt.subplots()
    i.plot.pie()
    st.pyplot(fig)


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