import streamlit as st

st.write(""" Box Office Predictions """)

genres = st.multiselect('Select genres:', ['Action', 'Comedy', 'Romance', 'Sci-fi'])

budget = st.number_input('Budget', step=100000)

collection = st.radio("Part of a collection: ", ('Yes', 'No'))

production_comp = st.selectbox("Production company", ['Disney', 'None'])
