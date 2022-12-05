import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def drawpie(i):
    fig, ax = plt.subplots()
    i.plot.pie()
    st.pyplot(fig)

def drawbar(x,y):
    fig, ax = plt.subplots()
    plt.bar(x,y)
    st.pyplot(fig)

def drawline(x,y):
    fig, ax = plt.subplots()
    plt.plot(x,y)
    st.pyplot(fig)