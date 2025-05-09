from dotenv import load_dotenv
load_dotenv() # Activate the local Env Var

import streamlit as st
import google.generativeai as genai
from pdf import read_pdf
from analysis import profile

#Create the Front End Page....
st.header("Resume Analysis:blue[Your Job Companion] Using AI 📑",divider="orange")
st.subheader("Tips for Using the Application")

#Resume part
st.sidebar.subheader("Upload the Resume 📝")
resume = st.sidebar.file_uploader(label="Upload your resume",type=['pdf'])
notes = f'''
* ** Upload the Resume**: Please Upload your Resume. This is a GEN AI App to extract insights
* ** Job Description**:Copy Paste the Job Description from Job Board.
* ** Unleash the Power of Gen AI Model**: Click the Button to generate Insights.'''
st.write(notes)

#JobDesc
st.subheader("Enter the Job Description",divider=True)
job_desc = st.text_area(label = "Copy Paste Job Description",max_chars=10000)
button = st.button(label="Get AI Powered Insights")
if button:
    st.markdown(profile(resume=resume,job_desc=job_desc))
    