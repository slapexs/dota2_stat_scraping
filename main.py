import requests
from bs4 import BeautifulSoup

url = 'https://liquipedia.net/dota2/ESL_One/Malaysia/2022/Statistics'
res_data = requests.get(url)

# Select data
raw_data = BeautifulSoup(res_data.text, 'html.parser')
