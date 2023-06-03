import streamlit as st
import pandas as pd

food = st.radio(
    "What's your favorite food",
    ('Pizza', 'Sushi', 'Monhinga'))

if food == 'Pizza':
    st.write('You like Italian food.')
elif food == 'Sushi':
    st.write('You like Japanese food.')
elif food == 'Monhinga':
    st.write("You like Burmese food.")

    
uploaded_files = st.file_uploader("Choose your favourite food image", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
    
options = st.multiselect(
    'Which file do you want to download?',
    ['Receipe', 'Ingredients List', 'Plating Design', 'Instructions'],
    ['Receipe', 'Ingredients List'])

st.write('You selected:', options)
    

text_contents = '''This is some text'''
st.download_button('Download receipe of your favourite food', text_contents)

text_contents = '''This is some text'''
st.download_button('Download Ingredients List of your favourite food', text_contents)

img_file_buffer = st.camera_input("Take a picture of your dish")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))


