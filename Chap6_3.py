# C:\Users\ephra\Documents\myScript\Streamlit>C:\Users\ephra\anaconda3\Scripts\activate.bat
# (base) C:\Users\ephra\Documents\myScript\Streamlit>activate py314
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>streamlit run Chap6_3.py

import streamlit as st

st.title("Streamlit Media and Interactivity Example")
tab1, tab2 = st.tabs(["Media", "Interactivity"])

with tab1:
    st.header("Media Examples")
    st.write("Here you can see examples of images, audio, and video in Streamlit.")
    
    # Image example
    st.subheader("Image Example")
    st.image("alexander-mass-E7HZMn2Gb5o-unsplash.jpg", caption="Example Image")
    
    # Audio example
    st.subheader("Audio Example")
    audio_file = open('D:/MyDocument/MP3/2 days into college new.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    
    # Video example
    st.subheader("Video Example")
    video_file = open("D:/MyDocument/Video/阿拉木圖/DJI_0338.MP4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)
    
with tab2:
    st.header("Interactivity Examples")
    st.write("Here you can see examples of buttons, selectboxes, and checkboxes in Streamlit.")
    
    # Button example
    st.subheader("Button Example")
    if st.button("Click me!"):
        st.write("Button clicked!")
    
    # Selectbox example
    st.subheader("Selectbox Example")
    city = st.selectbox("Select a city", ["New York", "London", "Tokyo"])
    st.write(f"You selected: {city}")
    
    # Checkbox example
    st.subheader("Checkbox Example")
    if st.checkbox("Show more options"):
        st.write("Here are more options!")
        st.write("- Option 1")
        st.write("- Option 2")
        st.write("- Option 3")
