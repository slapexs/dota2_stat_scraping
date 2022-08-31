import requests

url = 'https://liquipedia.net/dota2/ESL_One/Malaysia/2022/Statistics'
res_data = requests.get(url)
print(res_data)