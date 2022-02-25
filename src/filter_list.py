import json

input = "results/base_billionaires.json"
output = "results/filtered_billionaires.json"

with open(input, "r") as f:
    billionaire_dict = json.loads(f.read())

clean_billionaire_dict = {}
for k, v in billionaire_dict.items():

    if "Category:" in k:
        pass
    elif "List" in k:
        pass
    else:
        clean_billionaire_dict[k] = v

with open(output, "w+") as f:
    f.write(json.dumps(clean_billionaire_dict, indent=4))
