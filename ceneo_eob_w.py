# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:51:49 2020

@author: ANowakowska
"""


import time
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

czas = time.localtime()
data = str(str(czas[0])+"_"+str(czas[1])+"_"+str(czas[2]))


# tworzenie pliku
filename = 'eobuwie_ceneo_w_{p}.csv'.format(p=data)
f = open(filename, 'w')


# naglowki
headers = " Nazwa; Cena \n"
f.write(headers)

my_url = 'https://www.ceneo.pl/Moda;2804-0v;0020-200-0-0-0.htm'

# opening website, grabing
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
# html parsing
page_soup = soup(page_html, 'html.parser')

# podanie ilosci stron
ilosc_stron1 = page_soup.find_all("input", {"class": "js_pagination-top-input"})
    
for strona in page_soup.find_all("input", {"class": "js_pagination-top-input"}):
    ilosc_stron = strona.get("data-pagecount")
    
     
for i in range(int(ilosc_stron)):
    my_url = my_url
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    buty = page_soup.findAll("div", {"class": "grid-item__caption js_grid-item__caption"})
        
        
        
    for but in buty:
        if but.find("span", {"class": "category-item-additional-txt"}).text =="":
           nazwa = but.find("strong", {"class": "grid-item__name"}).text  
        else:
            nazwa = but.find("span", {"class": "category-item-additional-txt"}).text            
        cena_1 = but.find("span", {"class": "value"}).text
        cena_2 = but.find("span", {"class": "penny"}).text
        try:
            f.write(str(nazwa) + ";" + str(cena_1) + str(cena_2) + "\n")
        except UnicodeEncodeError:
            f.write("Błąd" + ";" + "Błąd" + ";" + "\n")    
                
       
        my_url = 'https://www.ceneo.pl/Moda;2804-0v;0020-200-0-0-{p:s}.htm'.format(p=str(i+1))
       
         
f.close()
       
        
        
