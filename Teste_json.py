import json
name = "cadastro.json"

with open(name, "r") as json_file:
    data = json.load(json_file)
    print(data)
