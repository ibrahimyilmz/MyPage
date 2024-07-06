import streamlit as st
from PIL import Image

image = Image.open("images/MyPhoto.png")

col1, col2 = st.columns(2)

with col1:
    st.image(image, use_column_width=True)

with col2:
    st.header("Ibrahim Enes Yılmaz")
    content = """
            Hello! I am a computer science student studying at Bilkent University. I am at my 2nd year. I have
            intermediate knowledge on python and java. In this page you can see the projects i have done.
            """
    st.info(content)

