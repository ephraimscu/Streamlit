# C:\Users\ephra\Documents\myScript\Streamlit>C:\Users\ephra\anaconda3\Scripts\activate.bat
# (base) C:\Users\ephra\Documents\myScript\Streamlit>activate py314
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>streamlit run Chap6_5.py


import streamlit as st
import time

placeholder = st.empty()
placeholder.write("Loading...")
time.sleep(2)  # Simulate a long-running process
placeholder.write("Content loaded successfully!")

placeholder.line_chart({"data": [5, 2, 3, 4, 5, 2,4,7,3,6]})
time.sleep(2)  # Simulate another long-running process
placeholder.write("Chart updated with new data!")

with placeholder.container():
    st.write("This is a container inside the placeholder.")
    st.write("You can add multiple elements here, and they will all be updated together when the placeholder is updated.")  

time.sleep(2)  # Simulate another long-running process
with placeholder:
    for seconds in range(5,0,-1):
        st.write(f"Updating in {seconds} seconds...")
        time.sleep(1)

placeholder.write("Update complete!")
placeholder.empty()  # Clear the placeholder content