import requests
from pprint import pprint

url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)

for item in resp.json():
    if item['name'] == 'Hulk':
        Hulk_intelligence = item['powerstats']['intelligence']
        
    if item['name'] == 'Captain America':
        Captain_intelligence = item['powerstats']['intelligence']
        
    if item['name'] == 'Thanos':
        Thanos_intelligence = item['powerstats']['intelligence']
        
max_intelligence = max(Hulk_intelligence, Captain_intelligence, Thanos_intelligence)

if Hulk_intelligence == max_intelligence:
    pprint(f'Самый умный Hulk c интеллектом {Hulk_intelligence} ед.')
if Captain_intelligence == max_intelligence:
    pprint(f'Самый умный Captain America c интеллектом {Captain_intelligence} ед.')
if Thanos_intelligence == max_intelligence:
    pprint(f'Самый умный Thanos c интеллектом {Thanos_intelligence} ед.')
    

        