"""
Title: CS Toolbox Methodology Guide - Quiz Script
Author: Grace Saville
Date: 3/3/2025
Summary: This script runs a quiz in Streamlit, and takes the questions from the "questions_json" file, and the resulting
information from the "methodology_projects_overview" csv.
"""
import streamlit as st
import pandas as pd
import requests
import json

# ---- DATA URLS ----
# Replace with your actual GitHub raw URLs
#DATA_URL = "https://raw.githubusercontent.com/your-repo/main/data.csv"
#QUESTIONS_URL = "https://raw.githubusercontent.com/your-repo/main/questions.json"

# ---- LOAD DATA ----
#@st.cache_data
#def load_data(url):
#    return pd.read_csv(url)

#@st.cache_data
#def load_questions(url):
#    response = requests.get(url)
#    return json.loads(response.text)

#proj_df = load_data(DATA_URL)
#questions = load_questions(QUESTIONS_URL)

@st.cache_data # caches the df so the app runs better
def load_data():
    return pd.read_csv("methodology_projects_overview.csv")  # read df with project information
proj_df = load_data()
# proj_df = pd.read_csv("methodology_projects_overview.csv")

# read json with quiz question dictionary in it:
with open("questions_json.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

# ---- UNIQUE VALUE OPTION ASSIGNMENT ----
# Getting unique values
unique_themes = proj_df["theme"].unique().tolist() # q2
unique_regions = proj_df["region"].unique().tolist() # q3

# Replacing "__UNIQUE_VALUES__" with actual values from project df
questions["q2"]["options"] = unique_themes # q2
questions["q2"]["options"].append("I'm not sure yet") # q2
questions["q3"]["options"] = unique_regions # q3
questions["q3"]["options"].append("I'm not sure yet") # q3

# ---- SESSION STATE INITIALIZATION ----
# Initialising session state, so that re-runs of the script in the same window keep responses
if "responses" not in st.session_state:
    st.session_state.responses = {} # "if dictionary of responses doesn't already exist, make one."

# ---- ASK QUESTIONS ----
st.title("Citizen Science Methodology and Project Guide")

for q_id, q in questions.items():
    q_number = q["number"]
    q_text = q["text"]
    q_type = q["type"]
    q_options = q["options"]

    # Displaying question based on its type
    if q_type == "single":
        st.session_state.responses[q_number] = st.radio(q_text, q_options)
    elif q_type == "multiple":
        st.session_state.responses[q_number] = st.multiselect(q_text, q_options)
    elif q_type == "dropdown":
        st.session_state.responses[q_number] = st.selectbox(q_text, q_options)

# ---- FILTER DATA ----
filtered_df = proj_df.copy()

for q_id, q in questions.items():
    q_number = q["number"]
    q_col = q["proj_column"]
    options_map = q["options"]  # Mapping from quiz answers to DF values

    if q_number in st.session_state.responses:
        user_answer = st.session_state.responses[q_number]

        # Converting user answer to the df value stored in the json
        if isinstance(options_map, dict):  # checking if there's a key-value pair in the json
            mapped_answer = options_map.get(user_answer, user_answer)
        else:  # if it's just a list in the json:
            mapped_answer = user_answer

        if mapped_answer and mapped_answer != "No":  # if answer exists and is not "No" (don't want it to filter the df)
            if mapped_answer == "Yes":  # Single choice
                filtered_df = filtered_df[filtered_df[q_col] == mapped_answer]
            elif isinstance(mapped_answer, list):  # Multiple choice
                filtered_df = filtered_df[filtered_df[q_col].isin(mapped_answer)]


# ---- DISPLAY RESULTS ----
st.write("### Recommended Projects/Methods:")
st.dataframe(filtered_df)





