# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:22:02 2024

@author: Dell
"""

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import math
# This function defines all 4 operations
def apogee(a, e):
    return a*(1+e)
def perigee(a, e):
    return a*(1-e)

def orbitaltime(apo,peri):
    c = (apo + peri + 12742)/2
    t = 6.28* math.sqrt((c*c*c)/398000)
    return t


def orbitalvelocity(rad,axis):
    c =  (2/rad)- (1/axis)
    vel = 19950 * math.sqrt(c)
    return vel

perigeeres =0
apogeeres =0
# Set page configuration
st.set_page_config(page_title="Space App",
                   layout="wide",
                   page_icon="")
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))



#sidebar for navigation
with st.sidebar:
    selected = option_menu('Orbit Calculations',

                           ['Apogee Calculation',
                            'Perigee Calculation',
                            'orbital Period',
                            'orbital velocity'
                           ],
                           menu_icon='rocket takeoff',
                           icons=['calculator', 'globe-americas' ,'infinity','percent'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Apogee Calculation':

  
        # page title
        st.title('Apogee Information')

       

        e = st.number_input('Enter Eccentricity')

        a = st.number_input('Enter semi-major axis (in kms)')
        if st.button('Calculate Apogee (in kms)'):

          

          apogeeres = apogee(a,e)

           

        st.success(apogeeres)

  

# Heart Disease Prediction Page
if selected == 'Perigee Calculation':

    # page title
        st.title('Perigee Calculation')

    
        e = st.number_input('Enter Eccentricity')

        a = st.number_input('Enter semi-major axis(in kms)')
      
        if st.button('Calculate Perigee'):

          

          perigeeres = perigee(a,e)

           

        st.success(perigeeres)
if selected == 'orbital Period':
    st.title('orbital Period')
    apo = st.number_input('Enter Apogee(in kms)')

    peri = st.number_input('Enter Perigee(in kms)')
  
    if st.button('Calculate Orbital Time Period(in kms)'):

      

      perigeeres = orbitaltime(apo, peri)

       

    st.success(perigeeres)
    
if selected == 'orbital velocity':

    st.title('Calculate Orbital Velocity')
    rad = st.number_input('Enter Apogee(in kms)')

    axis = st.number_input('Enter Perigee(in kms)')
  
    if st.button('Calculate Orbital Velocity'):

      

      perigeeres = orbitalvelocity(rad,axis)

       

    st.success(perigeeres)


   