# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 11:40:32 2019

@author: Omkar Nallagoni
"""




import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
import streamlit.components.v1 as com

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("food_delivery.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Age, Gender, Marital_Status, 
                                Occupation,Monthly_Income , Educational_Qualifications, 
                                Family_size, Pin_code,
                                Output):
   
    prediction=classifier.predict([[Age, Gender, Marital_Status, 
                                Occupation,Monthly_Income , Educational_Qualifications, 
                                Family_size, Pin_code,
                                Output]])
    print(prediction)
    return prediction
my_dictionary={
'male': 1,
 'female': 0,
 'single': 2,
 'married': 0,
 'prefer not to say': 1,
 'student': 3,
 'employee': 0,
 'self employeed': 2,
 'house wife': 1,
 'no income': 4,
 '25001 to 50000': 1,
 'more than 50000': 3,
 '10001 to 25000': 0,
 'below rs.10000': 2,
 'graduate': 0,
 'post graduate': 2,
 'ph.d': 1,
 'school': 3,
 'uneducated': 4,
 'yes': 1,
 'no': 0,
 'positive': 1,
 'negative ': 0}

def salary(my_sal):
    if int(my_sal)<10000:
        return 2
    elif int(my_sal)>=10001 and int(my_sal)<=25000:
        return 0
    elif int(my_sal) >=25001 and  int(my_sal)<=50000:
        return 1
    else:
        return 3
salary(20000)
def main():
    
    
    html_temp="""
     <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">ONLINE FOOD DELIVERY PLATFORMS FEEDBACK APP </h2>
    </div>
       """

    st.markdown(html_temp,unsafe_allow_html=True)

    Age = st.text_input("Age","Type Here")
    Gender = st.text_input("Gender","Type Here").lower()
    marital_attributes=[' ','single','married','prefer not to say']
    Marital_Status = st.selectbox("Marital status",marital_attributes)
    Occupation_attributes=['','student','employee','self employeed','house wife']
    Occupation = st.selectbox("Occupation",Occupation_attributes)
    Monthly_Income = st.text_input("Monthly income ","Type Here")
    Educational_Qualifications_attributes=[' ','graduate','post graduate','ph.d','school','uneducated']
    Educational_Qualifications = st.selectbox("Educational_Qualifications",Educational_Qualifications_attributes)
    Family_size = st.text_input("Family_size","Type Here")
    Pin_code = st.text_input("Pin_code","Type Here")
    output_attributes=['','yes','no']
    Output = st.selectbox("ouput(ordered again or not?)",output_attributes)
    try:
        result=""
        if st.button("Predict"):
            result=predict_note_authentication(eval(Age), my_dictionary[Gender], my_dictionary[Marital_Status], 
                                            my_dictionary[Occupation],salary(Monthly_Income), my_dictionary[Educational_Qualifications], 
                                            eval(Family_size), eval(Pin_code),
                                            my_dictionary[Output])
            if result==1:
                st.success('POSTIVE FEEDBACK')
            else:
                st.sucess('NEGATIVE FEEDBACK')
    except:
        st.error("please enter correct details or check the spellings ")

if __name__=='__main__':
    main()
    
    
    