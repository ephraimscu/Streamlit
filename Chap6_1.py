# C:\Users\ephra\Documents\myScript\Streamlit>C:\Users\ephra\anaconda3\Scripts\activate.bat
# (base) C:\Users\ephra\Documents\myScript\Streamlit>activate py314
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>streamlit run Chap6-7.py

import streamlit as st

page = st.sidebar.selectbox("Select a page", ["Page 1", "Page 2"])


if st.sidebar.button("Go to"):
    st.write(f"You selected: {page}")
    if page == "Page 1":
        st.title("Welcome to Page 1")
        st.write("This is the content of Page 1.")
    elif page == "Page 2":
        st.title("Welcome to Page 2")
        st.write("This is the content of Page 2.")


add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

with st.sidebar:
    add_radio = st.radio("Choose a contact method:", ("Email", "Home phone", "Mobile phone"))
    st.write(f"You selected: {add_selectbox}")
    st.write(f"You selected: {add_radio}")


