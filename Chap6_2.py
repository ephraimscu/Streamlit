# C:\Users\ephra\Documents\myScript\Streamlit>C:\Users\ephra\anaconda3\Scripts\activate.bat
# (base) C:\Users\ephra\Documents\myScript\Streamlit>activate py314
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>streamlit run Chap6_2.py

import streamlit as st
st.title("Streamlit Sidebar Example")

col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("This is the first column.")
    
with col2:
    st.header("Column 2")
    st.write("This is the second column.")
