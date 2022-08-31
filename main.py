from operator import index
import requests
from bs4 import BeautifulSoup

url = 'https://liquipedia.net/dota2/ESL_One/Malaysia/2022/Statistics'
res_data = requests.get(url)

# Select data
raw_data = BeautifulSoup(res_data.text, 'html.parser')

# Find data from html tag
table = raw_data.find('table')
tr = table.find_all('tr', {'class':'dota-stat-row'})

def findDataFromTr(trList):
    td = trList.find_all('td')
    temp = []
    for index in range(len(td)):
        temp.append(td[index].text.strip())
    return temp

for data in tr:
    response = findDataFromTr(data)
    


