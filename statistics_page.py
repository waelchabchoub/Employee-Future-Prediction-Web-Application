import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

data = pd.read_csv("Employee.csv").drop('City',axis=1).drop('JoiningYear',axis=1)

def show_statistics_page():
    st.title("Statistics")
    st.write("#### Leaving Employee Per Paymenet Tier")
    fig = plt.figure(figsize=(10,5))
    sns.countplot(data=data,x='PaymentTier',hue='LeaveOrNot')   
    st.pyplot(fig)
 
    st.write("#### Leaving Employee Per Age")
    fig = plt.figure(figsize=(10,5))
    sns.countplot(data=data,x='Age',hue='LeaveOrNot')  
    st.pyplot(fig)

    st.write("#### Leaving Employee Per Gender")
    fig = plt.figure(figsize=(10,5))
    sns.countplot(data=data,x='Gender',hue='LeaveOrNot')   
    st.pyplot(fig)

    st.write("####  Leaving Employee Per Experience Year")
    fig = plt.figure(figsize=(10,5))
    sns.countplot(data=data,x='ExperienceInCurrentDomain',hue='LeaveOrNot',) 
    st.pyplot(fig)

