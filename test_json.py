import json

with open('ai.json', 'r') as json_file: 
    data = json.load(json_file) 

list = data["projects"]
dict = list[0]

name = dict["name"]
symptoms = dict["symptom"]
id = dict["id"]

#for symptom in symptoms:
#    print(symptom)

for i in range(len(symptoms)):
  print(symptoms[i])
