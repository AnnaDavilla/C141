
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd




bright_stars_url = 'https://pt.wikipedia.org/wiki/Lista_das_estrelas_mais_brilhantes'


page = requests.get(bright_stars_url)
#print(page)


soup = bs(page.text,'html.parser')


star_table = soup.find('table', attrs={'class':'wikitable'})
#print(star_table)




temp_list= []
table_rows = star_table.find_all('tr')




for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)




Star_names = []
Constelation = []
Magnitude_Ap = []
Bayer = []
Classification_esp = []
Distance =[]




for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Constelation.append(temp_list[i][2])
    Magnitude_Ap.append(temp_list[i][3])
    Bayer.append(temp_list[i][4])
    Classification_esp.append(temp_list[i][5])
    Distance.append(temp_list[i][6])


headers = ['Nome da estrela', 'Constelação', 'Magnitude Ap.', 'Bayer', 'Classificação','Distância']


df1 = pd.DataFrame(list(zip(Star_names, Constelation, Magnitude_Ap, Bayer, Classification_esp, Distance)), columns=headers)
print(df1)


df1.to_csv('estrelas_mais_brilhantes.csv')


