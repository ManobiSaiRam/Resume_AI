import google.generativeai as genai
from pdf import read_pdf
import streamlit as st
import os

genai.configure(api_key=os.getenv("Google-API-KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

#Read the pdf
def profile(resume,job_desc):
    if resume is not None:
        resume_doc = read_pdf(resume)
        st.markdown("Resume has been Uploaded")
    else:
        st.warning("Resume Missing")

    response = model.generate_content(f''' Act as an HR or Ops head in AI domain and compare {resume} with {job_desc} and suggest - Am I a Good Fit?''')
    ats_score = model.generate_content(f"Compare the {job_desc} with the resume {resume} and suggest the ATS Score of the resume (in percentage)")
    probability = model.generate_content(f"Compare the {job_desc} with the resume {resume} and suggest the probability (in percentage) of getting selected")
    keywords = model.generate_content(f"Compare the {job_desc} with the resume {resume} and do a Keyword Analysis and mention the Missing Keywords in Bullet Points")
    improvements = model.generate_content(f"Compare the {job_desc} with the resume {resume} and suggest Improvements in the resume that are aligned with Job Desc")
    projects = model.generate_content(f"Compare the {job_desc} with the resume {resume} and suggest Projects/ML Competitions that are aligned with JD. ")
    #return
    return(st.write(response.text), 
           st.write(ats_score.text),
           st.write(probability.text),
           st.write(keywords.text),
           st.write(improvements.text),
           st.write(projects.text))
                            