This is AI Based Resume Evaluator.

We used Gen-AI model to evaluate Job description 

In order to map the repository with VSCode, we write the following line of code 

https://github.com/ManobiSaiRam/Resume_AI.git

Create Virtual Environment. The Code : python -m venv  .venv

Activate Virtual Environment. source .venv/Scripts/activate

We also created a list of libraries that are need to be installed. requriements.txt file

Created a .env file where we updated the Google API GOOGLE-API-KEY = "your_google_api_key

Update the requirements.txt file with the required libraries/packages for the project.

We will be creating three files app.py, pdf.py and analysis.py

app.py - It will have the front end components and all the intelligence from pdf and analysis files will flow here

pdf.py - This file will be used for extracting the text from the resume.

analysis.py - This is where we will use Gen AI model to write prompts and generate the output.
