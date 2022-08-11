import json

with open("tutorial.json") as f:
    data = json.load(f)

print(data["1"])