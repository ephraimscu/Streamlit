# from time import time

import streamlit as st
import sympy as sp
from PIL import Image
import pandas as pd
from io import StringIO
from datetime import timedelta, date, time

st.title("My First Streamlit App")

# with open('alexander-mass-E7HZMn2Gb5o-unsplash.jpg', 'rb') as f:
#     image_data = f.read()

# st.image(image_data, caption='Streamlit App Image')

images = [
    'alexander-mass-E7HZMn2Gb5o-unsplash.jpg','doncoombez--crmdG87Kjw-unsplash.jpg']
for img in images:
    with open(img, 'rb') as f:
        image_data = Image.open(img)
        corp_image = image_data.resize((500, 500))  # 調整圖片大小
    
    st.image(image_data, caption=f'Streamlit Original Image: {img}')
    st.image(corp_image, caption=f'Streamlit crop Image: {img}')
    

audio_file = open('D:/MyDocument/MP3/2 days into college new.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')  

#download button
st.subheader("Download Button example")
with open("D:/MyDocument/MP3/2 days into college new.mp3", "rb") as f:
    audio_data = f.read()
st.download_button(
    label="Download Audio",
    data=audio_data,
    file_name="2_days_into_college_new.mp3",
    mime="audio/mp3"
)

# video_file = open("D:/MyDocument/Video/阿拉木圖/DJI_0338.MP4", "rb")
# video_bytes = video_file.read()
# st.video(video_bytes)

st.subheader("button example")
if st.button("Click me!"):
    st.write("Button clicked!")

# st.button("Click me too!", on_click=lambda: st.write("Another button clicked!"))   

def my_format_func(option):
    return f"Option: {option}"

st.header("Selectbox with Custom Format")
city = st.radio("Select a city", ["New York", "London", "Tokyo"], format_func=my_format_func)
st.write(f"You selected: {city}")

if city == "New York":
    st.write("You selected New York!")
elif city == "London":
    st.write("You selected London!")
else:
    st.write("You selected Tokyo!")

st.subheader("Checkbox example")
if st.checkbox("Show more options"):
    st.write("Here are more options!")
    st.write("- Option 1")
    st.write("- Option 2")
    st.write("- Option 3")

size = st.radio("Select a size", ["Small", "Medium", "Large"])
st.write(f"You selected: {size}")

st.subheader("Slider example")
age = st.slider("Select your age", 0, 100, 25) 
st.write(f"Your age is: {age}")

st.subheader("Slider example 2")
price = st.slider("Select the price", 0.0, 100.0, 50.0, 0.1)
st.write(f"The price is: ${price:.1f}")

st.subheader("Slider example 3")
quantity = st.slider("Select the quantity", 1, 100, (25,75))
st.write(f"The quantity is: {quantity}")

st.subheader("Slider example 4")
time = st.slider("Select the time", value =(time(10,30), time(12,45)) )
st.write(f"The time is: {time}")  



st.subheader("Checkbox example")
agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("Thank you for agreeing!")

st.subheader("Checkbox example 2")
results = st.checkbox("Show results")
if results:
    st.write("Here are the results!")
    st.write("- Result 1")
    st.write("- Result 2")
    st.write("- Result 3")
else:    st.write("Results are hidden.")

st.subheader("Checkbox example 3")
st.write("Do you want to see the details?")
check1 = st.checkbox("Swimming",value = True)
check2 = st.checkbox("Running")
check3 = st.checkbox("Cycling")


#multiselect
options = st.multiselect("Select your favorite fruits", ["Apple", "Banana", "Orange", "Grape"])
st.write(f"You selected: {options}")

st.subheader("Selectbox example")
options = ["Cat", "Dog", "Rabbit", "Hamster"]
animal = st.selectbox("Select an animal", options)
st.write(f"You selected: {animal}")


# select_slider
st.subheader("Select Slider example")
option = st.select_slider("Select a number", options=[1, 2, 3, 4, 5])
st.write(f"You selected: {option}")

st.subheader("Select Slider example 2")
fruit_dict = {
    "蘋果": ":apple:",
    "香蕉": ":banana:",
    "橙子": ":orange:",
    "葡萄": ":grape:"
}

options = fruit_dict.keys()
fruit = st.select_slider("Select a fruit", options=options)
st.write(f"You selected: {fruit}", fruit, fruit_dict[fruit])

my_range = range(1, 11)

numbers = st.select_slider("Select a number from 1 to 10", options=my_range, value = 5)
st.write(f"You selected: {numbers}", numbers * ":star:")

# download button
st.subheader("Download Button example")
test_content = "This is a test file for download."
st.download_button(
    label="Download Test File",
    data=test_content,
    file_name="test_file.txt",
    mime="text/plain"
)

# binary data download
st.subheader("Download Binary Data example")
binary_data = b"This is some binary data."
st.download_button(
    label="Download Binary Data",
    data=binary_data,
    file_name="binary_data.bin",
    mime="application/octet-stream"
)

# text input
st.subheader("Text Input example")
name = st.text_input("Enter your name", autocomplete="name")
st.write(f"Hello, {name}!")

st.subheader("Text Area example")
message = st.text_area("Enter your message", placeholder="Your message here")
st.write(f"Your message: {message}")

# number input
st.subheader("Number Input example")
number = st.number_input("Enter a number", min_value=0, max_value=100, value=50, step=1)
st.write(f"You entered: {number}")

# BMI
st.subheader("BMI Calculator")
weight = st.number_input("Enter your weight (kg)", min_value=0.0, max_value=300.0, value=70.0, step=0.1)
height = st.number_input("Enter your height (cm)", min_value=0.0, max_value=250.0, value=170.0, step=0.1)
if st.button("Calculate BMI") and height > 0:
    bmi = weight / ((height / 100) ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

# date/time input
st.subheader("Date Input example")
date = st.date_input("Select a date")
st.write(f"You selected: {date}")

st.subheader("Date Input example 2")
date_1, date_2 = st.date_input("Select a date range", value=(date, date + timedelta(days=7)))
st.write(f"You selected: {date_1} to {date_2}")

st.subheader("Time Input example")
time = st.time_input("Select a time")
st.write(f"You selected: {time}")

# file uploader
st.subheader("File Uploader example")
uploaded_file = st.file_uploader("Upload a file", type=["txt", "csv", "xlsx"])
if uploaded_file is not None:    
    st.write(f"File uploaded: {uploaded_file.name}")
    file_content = uploaded_file.read()
    st.write(f"File content (first 100 bytes): {file_content[:100]}")


