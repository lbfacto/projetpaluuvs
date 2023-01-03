# -*- coding: utf-8 -*-

"""
Creerle 02 janvier 2023 a 16:08
@autheur AbdoulayeBA MASTER2 BIG DATAUVS
Model regression lineaire sur les donneesnumeriques et continue
"""


#loaded_model = pickle.load(open('C:/projet/projetPlau/palu_uvs/streamlit_model_palu.pkl'))

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav','rb'))


# creating a function for Prediction


def palu_prediction(input_data):


    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

# change the input_data to a numpy array


#chargement des des donnees d'entree


    if(prediction[0]==0):
        return 'Antigene positif Personne atteint du paludisme'
    else:
        return 'Antigene negatif personne n_est pas atteint du paludisme'


def main():

#titre application
    st.title('Application de prediction du paludisme Senegal UVS')
    Age = st.text_input('Age')

    ratio =st.text_input('ratio')

    G6PD = st.text_input('G6PD')

    EP_6M_AVT = st.text_input('EP_6M_AVT')

    AcPf_6M_AVT = st.text_input('AcPf_6M_AVT')

    EP_1AN_AVT = st.text_input('EP_1AN_AVT')

    AcPf_1AN_AVT =st.text_input('AcPf_1AN_AVT')

    EP_6M_APR = st.text_input('EP_6M_APR')

    AcPf_6M_APR = st.text_input('AcPf_6M_APR')

    EP_1AN_APR = st.text_input('EP_1AN_APR')

    AcPf_1AN_APR = st.text_input('AcPf_1AN_APR')


    diagnosis = ''

    if st.button('Resultat Paludisme'):
        diagnosis = palu_prediction([Age,ratio,G6PD,EP_6M_AVT,AcPf_6M_AVT,EP_1AN_AVT,AcPf_1AN_AVT,EP_6M_APR	,AcPf_6M_APR,EP_1AN_APR	,AcPf_1AN_APR])
        st.success(diagnosis)



if __name__ == '__main__':
    main()



