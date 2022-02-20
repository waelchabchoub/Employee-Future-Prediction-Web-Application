import streamlit as st
from predict_page import show_predict_page
from statistics_page import show_statistics_page

page = st.sidebar.selectbox('Statistics Or Predict',("Predict","Statistics"))
if(page=='Predict'):
    show_predict_page()
else : 
    show_statistics_page()