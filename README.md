# Isir internship project


## Architecture

```
project
│   README.md
│   main.py
│
└───recommendation
│   │   recommender.py
│   │   cleaning.py
│   │   functions.py
│   │
│   └───database
│       │   music.csv
│       │   movie.csv
│       │   ...
│   
└───utils
│   │   input_reader.py
│   │   file_reader.py
│   │
│   └───network
│   |   │   file_sender.py
│   │
│   └───generator
│   |   │   question.py
│   |   │   xml_file.py
│   
└───decision
│   │   behaviour.py
│   
```

TODO List :
- Comment code


Behaviour :
- Warm :
  - Use the user's name
  - Be positive
  - Use pronouns more than nouns
  - Use verbs and short sentences
  - Look while listening
  -> Question pool :
    - Hi "user first name", ready for some questions about your music taste? Let's start! What do you think about .. music? Do you like it?
    - Then, do you enjoy listening for .. music?
    - I'm wondering if you like .. music?
    - Do you like ...
- Competent
  - Use you words
  - Look while speaking
  - Use you words
  - Use last name?
  -> Question pool :
    - The purpose of the questions will be to find which music fit your taste. Do you often listen for .. music?
    - The next question will be about .. music. Do you listen for it?
    - Do you like ...
