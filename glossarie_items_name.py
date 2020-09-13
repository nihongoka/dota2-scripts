import csv
import urllib.request
import json

url = 'https://api.stratz.com/api/v1/Item?languageId=0'

cells = []

with urllib.request.urlopen(url) as resp:
    data = json.load(resp)
    for key in data:
        if key in ['276']:
            continue
        try:
            d = data[key]
            if d['stat']['isRecipe']:
                continue
            name = d['displayName']
            cells.append([name, name])
        except KeyError:
            pass

with open('glossarie_items_name.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows(cells)