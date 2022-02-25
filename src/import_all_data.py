from wikidata.client import Client
import json

input = "results/filtered_billionaires.json"
output = "results/update_billionaires.qs"

with open(input, "r") as f:
    billionaire_dict = json.loads(f.read())

with open("results/full_billionaire_data.json", "a") as f:

    for k, v in billionaire_dict.items():

        client = Client()
        entity = client.get(v, load=True)
        print(entity.items())
        break
