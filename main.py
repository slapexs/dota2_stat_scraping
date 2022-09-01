import requests
from bs4 import BeautifulSoup
import pandas as pd

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

hero_name = []
# List of data picks
pick_played = []
pick_win = []
pick_lost = []
pick_winrate = []
pick_teamplayed = []

# List of Radiant pick
rd_played = []
rd_win = []
rd_lost = []
rd_winrate = []
rd_teamplayed = []

# Lost of Dire pick
dire_played = []
dire_win = []
dire_lost = []
dire_winrate = []
dire_teamplayed = []

# Append data into list
for data in tr:
    response = findDataFromTr(data)
    hero_name.append(response[1].strip())
    pick_played.append(int(response[2]))
    pick_win.append(int(response[3]))
    pick_lost.append(int(response[4]))
    pick_winrate.append(float(response[5].split('%')[0]) if response[5].split('%')[0] != '-' else 0)
    pick_teamplayed.append(float(response[6].split('%')[0]) if response[6].split('%')[0] != '-' else 0)

    # Radiant
    rd_played.append(int(response[7]))
    rd_win.append(int(response[8]))
    rd_lost.append(int(response[9]))
    rd_winrate.append(float(response[10].split('%')[0]) if response[10].split('%')[0] != '-' else 0)

    # Dire
    dire_played.append(int(response[11]))
    dire_win.append(int(response[12]))
    dire_lost.append(int(response[13]))
    dire_winrate.append(float(response[14].split('%')[0]) if response[14].split('%')[0] != '-' else 0)

# Create DataFrame with pandas
pickTable = pd.DataFrame({
    'Hero': hero_name,
    'Played': pick_played,
    'Win': pick_win,
    'Lost': pick_lost,
    'Winrate': pick_winrate,
    'Teamplayed': pick_teamplayed
})

# Radiant picks
rdTable = pd.DataFrame({
    'Hero': hero_name,
    'Played': rd_played,
    'Win': rd_win,
    'Lost': rd_lost,
    'Winrate': rd_winrate
})

# Dire picks
direTable = pd.DataFrame({
    'Hero': hero_name,
    'Played': dire_played,
    'Win': dire_win,
    'Lost': dire_lost,
    'Winrate': dire_winrate
})

# Export file
# CSV
# pickTable.to_csv('output/picks.csv', index=False, mode='w')
# print('Pick exported!')
# rdTable.to_csv('output/radiant.csv', mode='w', index=False)
direTable.to_csv('output/dire.csv', mode='w', index=False)