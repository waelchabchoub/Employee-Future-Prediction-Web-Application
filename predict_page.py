import streamlit as st
import pickle
import pandas as pd


def load_model():
    with open('emp_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

classifier = data["model"]
le_education = data["le_education"]
le_gender = data["le_gender"]
le_ever_benched = data["le_ever_benched"]

def show_predict_page():
    st.title("Employee Future Prediction")
    st.write("""Stay Or Leave ?""")
    educations =(
        "Bachelors",
        "Masters",
        "PHD",
    )
    genders=(
        "Male",
        "Female",
    )
    payement_tiers = (
        "Highest",
        "Mid Level",
        "Lowest",
    )
    ever_benched = (
        "Yes",
        "No"
    )
    gender = st.radio("Gender",genders)
    education = st.selectbox("Education",educations)
    age = st.slider("Age",22,45,35)
    experience = st.slider("Experience In Current Field",0,15,0)
    payement = st.radio("Payement Tier",payement_tiers)
    if(payement=="Highest"):
        payement = 1
    elif(payement=="Mid Level"):
        payement = 2
    else:
        payement = 3

    benched = st.radio("Ever Kept out of Project For One Month Or More",ever_benched)

    ok = st.button("Start Predicting")
    if ok:
        x = pd.DataFrame([[education,payement,age,gender,benched,experience]],columns =['Education','PaymentTier','Age','Gender','EverBenched','ExperienceInCurrentDomain'])
        x['Education']=le_education.fit_transform(x['Education'])
        x['Gender']=le_gender.fit_transform(x['Gender'])
        x['EverBenched']=le_ever_benched.fit_transform(x['EverBenched'])
        prediction = classifier.predict(x)
        if(prediction[0]==0):
            st.subheader("The Prediction : The Employee Will not Leave")
        else:   
            st.subheader("The Prediction : The Employee Will Leave")

    