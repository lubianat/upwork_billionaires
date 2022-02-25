import json

input = "results/filtered_billionaires.json"
output = "results/update_billionaires.qs"

with open(input, "r") as f:
    billionaire_dict = json.loads(f.read())

with open("results/update_billionaires.qs", "a") as f:

    for k, v in billionaire_dict.items():

        f.write(f"{v}|P31|Q1062083|S143|Q328\n")
