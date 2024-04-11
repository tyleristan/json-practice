import json

with open('/workspace/json-practice/data/schacon.repos.json', 'r') as file:
    data = json.load(file)



for i in data:
    name = i['name']
    html = i['html_url']
    update = i['updated_at']
    visibility = i['visibility']
    line = name,html,update,visibility
    print(line.partition(','))