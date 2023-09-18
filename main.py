import streamlit as st
import requests

api_key = "8zA53aEUYAqOTkjeonsgXWv8WOXjPVP9pSaW8eCZ"

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# make a request
response1=requests.get(url)

# get a dictionary as data
data = response1.json()

# Extract the image title, url and explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# download the image
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath,"wb") as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)









