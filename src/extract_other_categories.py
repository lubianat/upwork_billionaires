import requests
import time
from tqdm import tqdm
import json
url = "https://en.wikipedia.org/w/api.php?action=query"

params = {
    "format":"json",
    "list":"categorymembers",
    "cmtitle":"Category:Billionaires_by_nationality",
    "cmlimit": "500"
}
