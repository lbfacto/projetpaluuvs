# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:53:51 2022

@author: siddhardhan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

palu_model = pickle.load(open('trained_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:

    selected = option_menu('Paludisme Prediction System',
                            ['Paludisme Prediction'],
                            icons=['activity'],
                            default_index=0)



# Diabetes Prediction Page
if (selected == 'Paludisme Prediction'):

    # page title
    st.title('Paludisme Prediction using ML')


    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age')

    with col2:
        ratio = st.text_input('ratio')

    with col3:
        G6PD = st.text_input('G6PD')

    with col1:
        EP_6M_AVT = st.text_input('EP_6M_AVT')

    with col2:
        AcPf_6M_AVT = st.text_input('AcPf_6M_AVT ')

    with col3:
        EP_1AN_AVT = st.text_input('EP_1AN_AVT')

    with col1:
        AcPf_1AN_AVT = st.text_input('AcPf_1AN_AVT')

    with col2:
        EP_6M_APR = st.text_input('EP_6M_APR')
    with col3:
        AcPf_6M_APR = st.text_input('AcPf_6M_APR ')
    with col1:
        EP_1AN_APR =st.text_input('EP_1AN_APR')
    with col2:
        AcPf_1AN_APR = st.text_input('AcPf_1AN_APR')




    # code for Prediction
    palu_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        palu_prediction = palu_model.predict([[Age,ratio,G6PD,EP_6M_AVT,AcPf_6M_AVT,EP_1AN_AVT,AcPf_1AN_AVT,EP_6M_APR,AcPf_6M_APR,EP_1AN_APR,AcPf_1AN_APR]])
        if (palu_prediction[0] == 1):
            palu_diagnosis = 'la personne a pas le paludisme'
        else:
            palu_diagnosis = 'la personne a  le paludisme'

    st.success(palu_diagnosis)
