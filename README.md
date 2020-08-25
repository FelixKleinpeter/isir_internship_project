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
- Fix low amount of tag assignment
- Fix tag name issue (change the database itself)
- Create generator for repeat question based on behavior
- Create body behavior
  - Add smile
  - Add rest pose
  - Use a pool of gesture while talking
- Catch the end of Greta sentences
- Create a better interface
  - Make an introduction : ask user name and email address
  - Introduce the purpose of the experiment


Behaviour :
- Warm :
  - Use the user's name
  - Be positive
  - Use pronouns more than nouns
  - Use verbs and short sentences
  - Look while listening
- Competent
  - Use you words
  - Look while speaking
  - Use you words
  - Use last name?

  Emotion = "cross" -> A explorer
  Premiere partie :
  C:\Users\f\Desktop\Cours\StageChatbot\greta\greta\greta\bin\BehaviorPlanner\IntentionLexicon

  Competence = dominance 3.5 p.48
  p.86
  Beaucoup de gestes idéationels = WARM
  Positions de repos des bras -> A étudier
