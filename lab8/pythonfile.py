import json
import csv

with open('/workspace/json-practice/data/schacon.repos.json', 'r') as file:
    data = json.load(file)
with open('chacon.csv', mode='w') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for i in data[:5]:
        name = i['name']
        html = i['html_url']
        update = i['updated_at']
        visibility = i['visibility']
        line = [name,html,update,visibility]
        writer.writerow(line)


    