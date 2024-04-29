import streamlit as st
import streamlit.components.v1 as stc
from ml_app import run_ml_app
from ml2_app import run_ml2_app

html_temp = """
            <div style="padding:10px; background-color:3872fb; border-radius:10px;">
                <h1 style="color:white"> Car Prediction App </h1>
                <h4 style="color:white"> This App Belong to Marketing Team</h4>
            <div style="">
            """

desc_temp = """
                ### Car Prediction App 
                This app is used by Marketing Team to Car Price Prediction

                ### App Content
                - Exploratory Data Analysis
                - Machine Learning Section
            """
def main ():
    stc.html(html_temp)

    menu = ["Home", "EDA", "ML Section", "ML 2"]
    choice = st.sidebar.selectbox("menu", menu)
     
    if choice == "Home":
        st.subheader("Home")
        st.markdown(desc_temp, unsafe_allow_html=True)
        # Run EDA App
        print("EDA")
    elif choice == "ML Section": 
        # Run ML App
        run_ml_app()
        print("ML App")
    elif choice == "ML 2": 
        # Run ML App
        run_ml2_app()

if __name__ == '__main__':
            main ()