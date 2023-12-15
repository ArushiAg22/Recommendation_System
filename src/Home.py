import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page


st.title("Welcome to Recommendation System")

col1, col2 = st.columns([1,1])

# Load image from file
with col1:
    image = Image.open("Images/images (2).jpeg")  # Change this to the path of your image
    st.image(image)

# Load image from file
with col2:
    image = Image.open("Images/images (1).jpeg")  # Change this to the path of your image
    st.image(image)

image = Image.open("Images/images.jpeg")  # Change this to the path of your image
st.image(image, use_column_width =True)

st.write("What type of Recommendations would you like today?")
col3, col4, col5 = st.columns([1,1,1])

# Create buttons
with col3:
    button_a = st.button("Movies")
with col4:
    button_b = st.button("TV Shows")
with col5:
    button_c = st.button("Books")

# Handle button clicks and redirect to corresponding pages
if button_a:
    switch_page("Movies")   # Rerun the app to go to Page A
elif button_b:
    switch_page("TV Shows")  # Rerun the app to go to Page B
elif button_c:
    switch_page("Books")  # Rerun the app to go to Page C
