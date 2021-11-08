import streamlit as st
import json

from PIL import Image

img = Image.open("Movie.jpg")
st.image(img, width=200)
st.title(" Box Office Predictions ")

st.text_input("Name of movie", "Type here")

genres = st.multiselect('Select genres:', ['Action', 'Comedy', 'Romance', 'Sci-fi', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Thriller', 'Western', 'Other', 'Adventure', 'Documentary'])

for i in range (len(genres)):
    genres[i] =  "'name' :'" + genres[i]

jsonGenres = json.dumps(genres)

budget = st.number_input('Budget', step=100000)

collection = st.checkbox("Part of a collection: ")

collectionBool = 0
if collection:
    collectionBool = 1


production_comp = st.selectbox("Production company", ['Disney', 'Warner Bros', 'Universal' , 'Sony', 'Paramount', 'Miramax', 'Columbia', 'Tristar' ,'20th Century','Other'])

cast = st.text_input("Name of main actor")
cast2 = st.text_input("Name of supporting actor")
cast3 = st.text_input("Name of supporting actress")

castlist = []
if cast is not None:
    castlist.append(cast)
if cast2 is not None:
    castlist.append(cast2)
if cast3 is not None:
    castlist.append(cast3)


crew = st.text_input("Name of director")
crew2 = st.text_input("Name of producer")

crewlist = []
if crew is not None:
    crewlist.append(crew)
if crew2 is not None:
    crewlist.append(crew2)



keyword = st.text_input("Plot keyword")

language = st.selectbox("Language spoken", ['English', 'Other'])
original_language = st.selectbox("Original Language", ['en', 'other'])
popularity = st.slider("Expected Popularity", 0,100, 50 )
runtime = st.number_input('Runtime in minutes', step=1)
production_country = st.text_input("Production Country")

date = st.date_input("Release date")
revstring = "Calculated revenue :" 

if st.button("Calculate"):
    table.append(budget)
    table.append(genres)
    table.append(original_language)
    table.append(popularity)
    table.append(production_comp)
    table.append(production_country)
    table.append(original_language)
    table.append(keyword)
    table.append(castlist)
    table.append(crewlist)
    table.append(collectionBool)
    revstring = table

st.info(revstring)

st.info(collectionBool)
