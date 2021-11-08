import streamlit as st

from PIL import Image

img = Image.open("Movie.jpg")
st.image(img, width=200)
st.title(" Box Office Predictions ")

st.text_input("Name of movie", "Type here")

genres = st.multiselect('Select genres:', ['Action', 'Comedy', 'Romance', 'Sci-fi', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Thriller', 'Western', 'Other', 'Adventure', 'Documentary'])

budget = st.number_input('Budget', step=100000)

collection = st.checkbox("Part of a collection: ")

production_comp = st.selectbox("Production company", ['Disney', 'Warner Bros', 'Universal' , 'Sony', 'Paramount', 'Miramax', 'Columbia', 'Tristar' ,'20th Century','Other'])

cast = st.text_input("Name of main actor")
cast2 = st.text_input("Name of supporting actor")
cast3 = st.text_input("Name of supporting actress")

crew = st.text_input("Name of director")
crew2 = st.text_input("Name of producer")


keyword = st.text_input("Plot keyword")

language = st.selectbox("Language spoken", ['English', 'Other'])

runtime = st.number_input('Runtime in minutes', step=1)

date = st.date_input("Release date")

st.button("Calculate", on_click=st.info("Calculated revenue"))
