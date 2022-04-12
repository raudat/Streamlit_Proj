import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('model.pkl','rb'))


def main():
  st.header("Admission Predictor")
  st.header("Drop in your scores to predict admission")
  st.sidebar.header("What is this Project about?")
  st.sidebar.text("Web App used to predict admission")
  st.sidebar.header("About the Dataset")
  st.sidebar.text("The Model was made using the Admission_Predict.csv dataset from Kaggle")
  st.sidebar.header("About the Model")
  st.sidebar.text("The Web App uses Linear Regression to make predictions")

  
  st.text('Here you have to input your achievements to get the probability of admission')
  cgpa = st.slider("Enter Your CGPA",min_value=0.00, max_value=10.00)
  gre = st.slider("Enter your GRE Score",min_value=0,max_value=340)
  toefl = st.slider("Enter your TOEFL Score",min_value=0,max_value=120)
  research = st.selectbox("Do You have Research Experience (0 = NO, 1 = YES)",options=[0,1], index=0)
  uni_rating = st.slider("Rating of the University you wish to get in on a Scale 1-5",min_value=1,max_value=5)

  inputs = [[cgpa,gre,toefl,research,uni_rating]]

  if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(float)
    st.success('The Probability of getting admission is {}'.format(updated_res))


if __name__ =='__main__':
  main()