import requests
import time
from tqdm import tqdm
import json
from os.path import exists


def main():

    members = get_pages_under_category("Category:Billionaires_by_nationality")

    members_level_2_file = "results/billionaires.txt"
    file_exists = exists(members_level_2_file)

    if not file_exists:
        members_level_2 = []

        for category in tqdm(members):
            new_members_level_2 = get_pages_under_category(category)
            members_level_2.extend(new_members_level_2)
            time.sleep(0.2)

        with open(members_level_2_file, "w+") as f:
            f.write(json.dumps(members_level_2, indent=4))
    else:
        with open(members_level_2_file) as f:
            members_level_2 = json.loads(f.read())

    billionaires_dict = {}
    for members in tqdm(chunks(members_level_2, 50)):
        billionaires_dict.update(get_ids_from_pages(members_level_2))
        time.sleep(0.2)

    with open("results/base_billionaires.json", "w+") as f:
        f.write(json.dumps(billionaires_dict, indent=4))


def get_ids_from_pages(pages):
    """
    Returns a dictionary with page titles as keys and Wikidata QIDs as values
    """
    url = "https://en.wikipedia.org/w/api.php?action=query"
    params = {
        "format": "json",
        "prop": "pageprops",
        "ppprop": "wikibase_item",
        "redirects": "1",
        "titles": "|".join(pages),
    }
    r = requests.get(url, params)
    print(r)
    data = r.json()
    print(data)
    id_dict = {}
    for key, values in data["query"]["pages"].items():
        title = values["title"]
        qid = values["pageprops"]["wikibase_item"]
        id_dict[title] = qid

    return id_dict


def get_pages_under_category(category_name):
    url = "https://en.wikipedia.org/w/api.php?action=query"
    params = {
        "format": "json",
        "list": "categorymembers",
        "cmtitle": category_name,
        "cmlimit": "500",
    }
    r = requests.get(url, params)
    data = r.json()
    pages = []
    for response in data["query"]["categorymembers"]:
        pages.append(response["title"])
    while "continue" in data:
        params.update(data["continue"])
        r = requests.get(url, params)
        data = r.json()
        for response in data["query"]["categorymembers"]:
            pages.append(response["title"])
    return pages


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


if __name__ == "__main__":
    main()
