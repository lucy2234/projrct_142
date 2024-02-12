from bs4 import BeautifulSoup
import requests
import pandas as pd

url_path="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(url_path)
soup=BeautifulSoup(page.text,"html.praser")
star_table=soup.find_all("table")
temp_list=[]
table_rows=star_table[7].find_all("tr")

for tr in table_rows:
    tds=tr.find_all("tr")
    row=[i.text.rstrip()for i in tds]
    temp_list.append(row)

header=["brwn_draft","constellation"]

dawrf_brown=pd.DataFrame(temp_list,columns=header)
dawrf_brown.to_csv("new_dawrf_brown.csv",index=True,imdex_label="id")