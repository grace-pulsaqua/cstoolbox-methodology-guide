"""
Title: CS Toolbox Methodology Guide - Questions Script
Author: Grace Saville
Date: 3/3/2025
Summary: This script is designed to produce a json file for use in the quiz script. The questions, answers, and actions
can be edited here and will be written neatly to the json file, so that the file itself and the quiz script don't need
to be edited directly.
"""

import json

# methods: single, multiple, dropdown,

q1 = {
    "number": "1",
    "type": "single",
    "text": "In which area would you like assistance?",
    "options": ["I'm not sure yet",
                "I need help exploring current (local) environmental action initiatives",
                "I need help designing my own inspiring project"
                ],
    "proj_column": "type"
}

q2 = {
    "number": "2",
    "type": "single",
    "text": "Are you looking to design a project from scratch, or model yours after an existing project?",
    "options": {"I'm not sure yet": "No",
                "Design my own project": "Method",
                "Model my project after an existing project": "Project"
                },
    "proj_column": "type",
    "condition": {
        "question": "1",
        "value": "I need help designing my own inspiring project"
    }
}

q3 = {
    "number": "3",
    "type": "multiple",
    "text": "Is there a particular project theme you are interested in? Select one or all that apply.",
    "options": ["I'm not sure yet",
                "__UNIQUE_VALUES__" # df.colname.unique() (have script re-write the json if the unique values are not the same, or maybe load them as a variable beforehand)
                ],
    "proj_column": "theme"
}


q4 = {
    "number": "4",
    "type": "multiple",
    "text": "Are you looking for projects in a specific region?",
    "options": ["I'm not sure yet",
                "__UNIQUE_VALUES__"
                ],
    "proj_column": "region"
}

q5 = {
    "number": "5",
    "type": "single",
    "text": "Are you looking for a project that is currently active, or for example, are you looking for project inspiration irregardless of inactivity?",
    "options": {"I'm not sure yet": "No",
                "Active projects only": "Yes",
                "Any project, active or inactive": "No"
                },
    "proj_column": "currently_active_yn"
}

q6 = {
    "number": "6",
    "type": "single",
    "text": "Are you looking for a project which has material available for teaching school children or young adults?",
    "options": {"I'm not sure yet": "No",
                "Yes that would be helpful": "Yes",
                "Not per se": "No"
                },
    "proj_column": "teaching_material_yn"
}


q7 = {
    "number": "7",
    "type": "single",
    "text": "Are you looking for a project with open data, allowing you to download the data and analyse them yourself?",
    "options": {"I'm not sure yet": "No",
                "Yes, open data": "Yes",
                "Not per se": "No"
                },
    "proj_column": "open_data_download_yn"
}


q8 = {
    "number": "8",
    "type": "single",
    "text": "Are you looking for an phone app to assist with data collection?",
    "options": {"I'm not sure yet": "No",
                "Yes, I want an app to use": "Yes",
                "Not per se": "No"
                },
    "proj_column": "app_yn"
}



# Making the full set of questions a dictionary:
questions = {"q1": q1,
             "q2": q2,
             "q3": q3,
             "q4": q4,
             "q5": q5,
             "q6": q6,
             "q7": q7,
             "q8": q8}

# Writing the questions to a json file:
with open("questions_json.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=4)



'''
Notes:

CS Toolbox - methodology design help - possible guiding questions:

Overarching question: 
I have a scientific and/or environmental research question/hypothesis/idea/general curiousity and I would like to set up a citizen science project to help answer it. 
What citizen science methods, tools, and example projects are available to help me set up a CS project?


Citizen Science Draft Plan Design Tool/template:
Why are you measuring? What impact would you want to make if you could?
Do you already know what parameters you would like to measure? What are you going to measure?
Where and when will the measurements be taken, by whom and with what?
Which partners do you have (need) and which stakeholders are important?

check here: https://pulsaquanederland.sharepoint.com/:x:/s/PULSAQUA/ESqLrfr5CqJFvF_cWKkp3RoBPlkHNipAXjYeSN56FLimIw?e=yFCAib 

Describe the problem that you want to bring attention, urgency and/or change to.
Why is it a problem? You need to be very clear about why something is a problem. Because what you experience as a problem does not necessarily have to be the same for others.
What might be the reason for this problem? What is causing this problem?
Describe your goal. What do you want to change, if you succeed? What do you want to achieve with your monitoring initiative? What impact do you want to achieve? What advantage could you can achieve by monitoring/measuring? What change do you want to bring about, or rather put a stop to or prevent?
Now describe your research question. What question are you going to answer by monitoring? Make this as precise and detailed as possible.
'''
