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
    "options": ["I need help exploring current CS projects",
                "I need help designing my own CS project",
                "I'm not sure yet"
    ],
    "proj_column": "type"
}

q2 = {
    "number": "2",
    "type": "multiple",
    "text": "Is there a particular project theme you are interested in?",
    "options": ["__UNIQUE_VALUES__", # df.colname.unique() (have script re-write the json if the unique values are not the same, or maybe load them as a variable beforehand)
                "I'm not sure yet"
                ],
    "proj_column": "theme"
}


q3 = {
    "number": "3",
    "type": "multiple",
    "text": "Are you looking for projects in a specific country?",
    "options": ["__UNIQUE_VALUES__",
                "I'm not sure yet"
                ],
    "proj_column": "region"
}

q4 = {
    "number": "4",
    "type": "single",
    "text": "Are you looking for a project that is currently active, or for example, are you looking for project inspiration irregardless of inactivity?",
    "options": {"Active projects only":"Yes",
                "Any project, active or inactive":"No",
                "I'm not sure yet":"No"
                },
    "proj_column": "currently_active_yn"
}

q5 = {
    "number": "5",
    "type": "single",
    "text": "Are you looking for a project which has material available for teaching school children or young adults?",
    "options": {"Yes that would be helpful":"Yes",
                "Not per se":"No",
                "I'm not sure yet":"No"
                },
    "proj_column": "teaching_material_yn"
}


q6 = {
    "number": "6",
    "type": "single",
    "text": "Are you looking for a project with open data, allowing you to download the data and analyse them yourself?",
    "options": {"Yes, open data":"Yes",
                "Not per se":"No",
                "I'm not sure yet":"No"
                },
    "proj_column": "open_data_download_yn"
}


q7 = {
    "number": "7",
    "type": "single",
    "text": "Are you looking for an phone app to assist with data collection?",
    "options": {"Yes, I want an app to use":"Yes",
                "Not per se":"No",
                "I'm not sure yet":"No"
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
             "q7": q7}

# Writing the questions to a json file:
with open("questions_json.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=4)



'''
Notes:

CS Toolbox - methodology design help - possible guiding questions:

Overarching question: 
I have a scientific and/or environmental research question/hypothesis/idea/general curiousity and I would like to set up a citizen science project to help answer it. 
What citizen science methods, tools, and example projects are available to help me set up a CS project?

a. "I need help exploring current CS projects"
b. "I need help designing my own CS project"

a:

Is there a particular project theme you are interested in? select from...
Are you looking for projects in a specific country? select from...
Are you looking for a project that is currently active, or for example, are you looking for project inpiration irregardless of inactivity?
Are you looking for a project which has material available for teaching school children or teens?
Are you looking for a project with open data or a data map, allowing you to see results and/or analyse them yourself?


b:

Do you already have a (rough) plan or are you more interested in general information?
What theme does your project idea fall under?
Are you looking for a project with teaching material for children/young adults?
Are you looking to design a project from scratch, model yours after an existing project, or take part in an existing project?
Are you looking for an phone app to assist with data collection?
Would you like a measurement kit which automatically takes measurements for you, or do you expect to go out regularly to take the measurements personally?


Citizen Science Draft Plan Design Tool/template:
Why are you measuring? What impact do you really want to make?
Do you already know what parameters you would like to measure? What are you going to measure?
Where will you measure this?
When will you measure this?
What will you measure this with?
Who is going to do the measurements? You on your own? Or do you need help with that?
Which partners do you have (need) and which stakeholders are important?




Describe the problem that you want to bring attention, urgency and/or change to.
Why is it a problem? You need to be very clear about why something is a problem. Because what you experience as a problem does not necessarily have to be the same for others.
What might be the reason for this problem? What is causing this problem?
Describe your goal. What do you want to change, if you succeed? What do you want to achieve with your monitoring initiative? What impact do you want to achieve? What advantage could you can achieve by monitoring/measuring? What change do you want to bring about, or rather put a stop to or prevent?
Now describe your research question. What question are you going to answer by monitoring? Make this as precise and detailed as possible.
'''
