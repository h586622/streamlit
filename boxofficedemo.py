import streamlit as st

from PIL import Image

img = Image.open("Movie.jpg")
st.image(img, width=200)
st.title(" Box Office Predictions ")

st.text_input("Name of movie", "Type here")

genres = st.multiselect('Select genres:', ['Action', 'Comedy', 'Romance', 'Sci-fi', 'Horror', 'Adventure', 'Documentary'])

budget = st.number_input('Budget', step=100000)

collection = st.checkbox("Part of a collection: ")

production_comp = st.selectbox("Production company", ['Disney', 'None'])
