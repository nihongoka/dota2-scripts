import csv
import urllib.request
import json

url = 'https://api.stratz.com/api/v1/Ability?languageId=0'

cells = []

with urllib.request.urlopen(url) as resp:
    data = json.load(resp)
    for key in data:
        try:
            d = data[key]
            if d['isTalent']:
                continue
            if not d['drawMatchPage']:
                continue
            if not 'uri' in d:
                continue
            name = d['language']['displayName']
            if name == 'Empty':
                continue
            cells.append([name, name])
        except KeyError:
            pass

with open('glossarie_skills_name.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows(cells)