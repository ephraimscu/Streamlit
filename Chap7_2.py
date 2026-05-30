# C:\Users\ephra\Documents\myScript\Streamlit>C:\Users\ephra\anaconda3\Scripts\activate.bat
# (base) C:\Users\ephra\Documents\myScript\Streamlit>activate py314
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>streamlit run Chap7_2.py

import streamlit as st

name = st.text_input("Enter your name:", placeholder="Your name here")
if not name:
    st.warning("Please enter your name.")
    st.stop()  # Stop the execution of the app until the user enters their name

st.success(f"Hello, {name}! Welcome to Streamlit.")

st.title("Form Example")
with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    submit_button = st.form_submit_button("Submit")

if submit_button:
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")

with st.form("my_form_2"):
    st.write("This is another form.")
    slider_val = st.slider("Select a value", 0, 100, 50)
    checkbox_val = st.checkbox("Check me!")
    submit_button_2 = st.form_submit_button("Submit Form 2")
    
    if submit_button_2:
        st.write(f"Slider Value: {slider_val}")
        st.write(f"Checkbox Value: {checkbox_val}")

st.write("This is outside the forms and will always be displayed.")