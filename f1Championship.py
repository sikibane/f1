import pandas as pd
import requests
from bs4 import BeautifulSoup


data= pd.read_excel('F1 project final.xlsx',sheet_name='Final')
names=pd.read_excel('F1 project final.xlsx',sheet_name='Races')
names.rename(columns={'year':'season'},inplace=True)

merged=pd.merge(data,names,on=['season','round'],how='left')
merged.drop(merged.columns[3], axis=1, inplace=True)

race_data=merged.dropna(axis=0)



url='https://en.wikipedia.org/wiki/List_of_Formula_One_World_Drivers%27_Champions'
r= requests.get(url)
soup= BeautifulSoup(r.text,'html.parser') 
tr= soup.find_all('a')
for index,value in enumerate(tr):
    print(index)
    print(value)
print(tr)
len(tr)
type(tr)

nz=tr[1719:1852]
print(nz)

for index,value in enumerate(nz):
    print(index)
    print(value)

drivers=nz[1::2]
years=nz[2::1]

for index,value in enumerate(drivers):
    print(index)
    print(value)    
    
    
champions=[]

for x in drivers:
    text= x.text
    
    champions.append({'Name':text})
empty=[]    
for y in years:
    years= y.text
    
    empty.append({'years':years})
    
season=empty[0::2]

champion_data=pd.DataFrame.from_records(champions).join(pd.DataFrame.from_records(season))

champion_data['Name'] = champion_data['Name'].str.replace('K. Rosberg','keke_rosberg')
champion_data['Name'] = champion_data['Name'].str.replace('N. Piquet','piquet')
champion_data['Name'] = champion_data['Name'].str.replace('N. Lauda','lauda')
champion_data['Name'] = champion_data['Name'].str.replace('A. Prost','prost')
champion_data['Name'] = champion_data['Name'].str.replace('A. Senna','senna')
champion_data['Name'] = champion_data['Name'].str.replace('N. Mansell','mansell')
champion_data['Name'] = champion_data['Name'].str.replace('M. Schumacher','michael_schumacher')
champion_data['Name'] = champion_data['Name'].str.replace('D. Hill','damon_hill')
champion_data['Name'] = champion_data['Name'].str.replace('J. Villeneuve','villeneuve')
champion_data['Name'] = champion_data['Name'].str.replace('M. Häkkinen','hakkinen')
champion_data['Name'] = champion_data['Name'].str.replace('F. Alonso','alonso')
champion_data['Name'] = champion_data['Name'].str.replace('K. Räikkönen','raikkonen')
champion_data['Name'] = champion_data['Name'].str.replace('L. Hamilton','hamilton')
champion_data['Name'] = champion_data['Name'].str.replace('J. Button','button')
champion_data['Name'] = champion_data['Name'].str.replace('S. Vettel','vettel')
champion_data['Name'] = champion_data['Name'].str.replace('N. Rosberg','rosberg')

champion_data=champion_data[27:]










