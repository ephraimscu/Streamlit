# C:\Users\ephra\Documents\myScript\Streamlit>C:\Users\ephra\anaconda3\Scripts\activate.bat
# (base) C:\Users\ephra\Documents\myScript\Streamlit>activate py314
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>streamlit run Chap6_4.py

import streamlit as st

# expender

st.title("Streamlit Expander Example")
st.bar_chart({"data": [1, 2, 3, 4, 5]})
with st.expander("See explanation"):
    st.write("""
        The chart above shows a simple bar chart with data from 1 to 5.
        You can put any content you want inside the expander, including text, images, or even other charts.
    """)


st.subheader("Another Expander Example")
with st.expander("More details"):
    st.write("""
        This is another expander example. You can use expanders to hide content that might be too detailed or not immediately relevant to the user.
        Expanders help keep your app clean and organized while still providing access to additional information when needed.
    """)

st.subheader("Nested Expander Example")
with st.expander("Outer Expander"):
    st.write("This is the outer expander.")
    with st.expander("Inner Expander"):
        st.write("This is the inner expander. You can nest expanders to create a hierarchy of information.")

st.write("第一個外部文字")
container = st.container() 

container.write("第二個內部文字")

# 使用with語法增加文字
with container:
    st.image("https://www.python.org/static/community_logos/python-logo.png", width=200)
    
    if st.button("點擊我"):
        st.write("按鈕被點擊了！")
    st.write("Button is inside the container, so it will be displayed below the image and the text inside the container.")

st.write("第二個外部文字")
st.button("外部按鈕")
