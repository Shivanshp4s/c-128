from bs4 import BeautifulSoup
import requests
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# get page
page = requests.get(START_URL)

#pars page
soup = BeautifulSoup(page.text,'html.parser')

#get the table
star_table = soup.find_all('table',{"class" : "wikitable sortable"})
temp_list = []

table_rows = star_table[1].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star_names = []
distance = []
mass = []
radius = []

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

#convet to csv
headers = ['Star_names','Distance','Mass','Radius']

df2 = pd.DataFrame(list(zip(star_names,distance,mass,radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv', index=True, index_label="id")