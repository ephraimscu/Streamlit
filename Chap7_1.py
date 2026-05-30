# C:\Users\ephra\Documents\myScript\Streamlit>C:\Users\ephra\anaconda3\Scripts\activate.bat
# (base) C:\Users\ephra\Documents\myScript\Streamlit>activate py314
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>streamlit run Chap7_1.py
import time

import streamlit as st

st.header("Progress Bar Example")

progress_text_1 = "AI thinking..."

progress_bar = st.progress(0, text=progress_text_1)
my_bar = st.progress(0, text="Loading...")

time.sleep(2)  # Simulate a long-running process
progress_bar.progress(50, text=progress_text_1)

time.sleep(2)  # Simulate another long-running process
progress_bar.progress(100, text="AI has completed the task!")


for percent_complete in range(80):
    time.sleep(0.1)  # Simulate work being done
    my_bar.progress(percent_complete + 1, text=f"Loading... {percent_complete + 1}%")

for percent_complete in range(80, 99):
    time.sleep(0.1)  # Simulate work being done
    my_bar.progress(percent_complete + 1, text=f"Loading... {percent_complete + 1}%")

my_bar.progress(100, text="Loading complete!")

st.title("Progress Bar Example")
with st.spinner("AI thinking ..."):
    time.sleep(3)  # Simulate a long-running process
st.write("AI has completed the task!")

st.title("Progress Bar Example")
# 不可以使用表情符號短程是
st.error("Error message information",icon="🚨")
st.error("Error message information")
st.warning("Warning message information",icon="⚠️")
st.warning("Warning message information")
st.info("Info message information",icon="ℹ️")
st.info("Info message information")
st.success("Success message information",icon="✅")
st.success("Success message information")

#exception()方法用於顯示異常信息，通常用於捕獲和顯示錯誤訊息。
try:
    1 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    st.error("An error occurred: Division by zero.")
    st.exception(e)

