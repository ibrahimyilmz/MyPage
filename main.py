import streamlit as st
import pandas as pd

col1, col2 = st.columns(2)

with col1:
    st.image("images/MyPhoto.png", use_column_width=True)

with col2:
    st.header("Ibrahim Enes Yılmaz")
    content = """
            Hello! I am a computer science student studying at Bilkent University. I am at my 2nd year. I have
            intermediate knowledge on python and java. In this page you can see the projects i have done.
            """
    st.info(content)

st.write("Here you can find the projects i did so far.")

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df.iterrows():
        if index % 2 == 0:
            st.header(row["title"])
            st.image()

with col4:
    for index, row in df.iterrows():
        if index % 2 == 1:
            st.header(row["title"])
