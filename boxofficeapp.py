from pycaret.regression import load_model, predict_model 
import pandas as pd 
import numpy as np
import streamlit as st
from PIL import Image
import os

from google.colab import drive 
drive.mount('/content/drive')


from pycaret.regression import load_model, predict_model 
import pandas as pd 
import numpy as np
import streamlit as st
from PIL import Image
import os

class StreamlitApp:
    
    def __init__(self):
        self.model = load_model('drive/MyDrive/ColabNotebooks/BoxOfficeModel') 
        self.save_fn = 'path.csv'  

    def predict(self, input_data):
        return predict_model(self.model, data=input_data)

    def store_prediction(self, output_df): 
        if os.path.exists(self.save_fn):
            save_df = pd.read_csv(self.save_fn)
            save_df = save_df.append(output_df, ignore_index=True)
            save_df.to_csv(self.save_fn, index=False)
            
        else: 
            output_df.to_csv(self.save_fn, index=False) 
        
    def run(self):
        image = Image.open('drive/MyDrive/ColabNotebooks/boxoffice.png')
        image.resize = (400, 400)
        st.image(image, use_column_width=False)


        st.title(" Box Office Predictions ")
        title = st.text_input("Name of movie", "Type here")
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
        runtime = st.number_input('Runtime in minutes', step=1)
        date = st.date_input("Release date")
        st.button("Calculate")
        st.info(revstring)
        st.info(collectionBool)
        original_language = st.selectbox("Original Language", ['en', 'other'])
        popularity = st.select_slider("Expected Popularity", 0,100 )
        production_country = st.text_input("Production Country")
        status = st.selectbox("Released", ['1','0'])

        revstring = "Calculated revenue :" 


        if st.button("Calculate"):    
            input_dict = {'budget':budget, 'genres':genres, 'belongs_to_collection': collectionBool, 'status': status, 'crew': crew, 'cast': cast, 'original_language': original_language, 'keywords': keyword, 'spoken_language': original_language, 'production_countries': production_country, 'original_title': title, 'production_companies': production_comp, 'popularity': popularity, 'runtime': runtime, 'release_date': date } 
            input_df = pd.DataFrame(input_dict, index=[0])
            output = model.predict(input_df)
            revstring = predict_model(model, data=input_dict)

        st.success('Predicted output: {}'.format(output))

sa = StreamlitApp()
sa.run()

