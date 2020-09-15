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
- Create body behavior
  - Add rest pose
  - Increase gesture pool
- Catch the end of Greta sentences
- Create a better interface
  - Introduce the purpose of the experiment
  - Add button choice
- Fix architecture
- Gather results


-> restpose

Behaviour :
- Warm :
  - Use the user's name
  - Be positive
  - Use pronouns more than nouns
  - Use verbs and short sentences
  - Look while listening

  - Use "I" more than "us"
  - Less synonyms -> give the impression that phrases are less meditated
- Competent
  - Use you words
  - Look while speaking
  - Use you words
  - Use last name?

  - Avoid pronouns to make sentences longer

  Emotion = "cross" -> A explorer
  Premiere partie :
  C:\Users\f\Desktop\Cours\StageChatbot\greta\greta\greta\bin\BehaviorPlanner\IntentionLexicon

  Competence = dominance 3.5 p.48
  p.86
  Beaucoup de gestes idéationels = WARM
  Positions de repos des bras -> A étudier


  -> Remove electronica (gather it with electronic)
  -> Remove alternative?
  -> Artiste sans nom à enlever
