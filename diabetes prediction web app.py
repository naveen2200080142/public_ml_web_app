

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('C:/Users/navee/.spyder-py3/trained_model (1).sav','rb'))
def diabetes_prediction(input_data): 
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # standardize the input data

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      print('The person is not diabetic')
    else:
      print('The person is diabetic')
def main():
    st.title("diabates prediction web app")
    
    Pregnencies=st.text_input("Nnumber of Pregnecies")
    Glucose=st.text_input("glucose level")
    BloodPressure=st.text_input("Blood Pressure value")
    SkinThickness=st.text_input("Skin Thikness value")
    Insulin=st.text_input("Insulin level")
    BMI=st.text_input("BMI value")
    DiabetespedigreeFunction=st.text_input("DiabetespedigreeFunction value")
    Age=st.text_input("Age of the Person")
    diagnosis=''
    #creating a button
    if st.button('Diabetes test Rexult'):
        diagnois=diabetes_prediction([Pregnencies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetespedigreeFunction,Age])
    st.success(diagnosis)
if __name__=='__main__':
    main()
      