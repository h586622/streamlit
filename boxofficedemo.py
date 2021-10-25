import streamlit as st

st.write(""" my first app""")

genres = st.multiselect('Select genres:', ['Action', 'Comedy', 'Romance', 'Sci-fi'])

budget = st.number_input('Budget')
