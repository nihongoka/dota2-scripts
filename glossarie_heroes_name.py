import csv
import urllib.request
import json

url = 'https://api.stratz.com/api/v1/Hero?languageId=0'

cells = []

with urllib.request.urlopen(url) as resp:
    data = json.load(resp)
    for key in data:
        try:
            d = data[key]
            name = d['displayName']
            cells.append([name, name])
        except KeyError:
            pass

with open('glossarie_heores_name.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows(cells)