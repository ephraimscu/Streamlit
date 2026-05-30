# C:\Users\ephra\Documents\myScript\Streamlit>C:\Users\ephra\anaconda3\Scripts\activate.bat
# (base) C:\Users\ephra\Documents\myScript\Streamlit>activate py314
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>streamlit run login.py

import streamlit as st

st.title("Login Form")

if not st.user.get("logged_in"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.email = "admin@example.com"
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password.")
            st.stop()

        st.write("Welcome to the app! You are logged in.")
        st.write("Username:", st.session_state.get("username"))
        st.write("Email：", st.session_state.get("email"))


        st.button("logout", on_click=st.logout)
        if not st.session_state.get("logged_in"):
            st.button("Login Again", on_click=st.login)
            st.warning("You have been logged out.")
            st.stop()

        st.stop()