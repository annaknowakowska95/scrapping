# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:25:45 2021

@author: anowakowska
"""



import time
from urllib.request import urlopen as uReq, Request as Req
from bs4 import BeautifulSoup as soup

czas = time.localtime()
data = str(str(czas[0])+"_"+str(czas[1])+"_"+str(czas[2]))


# tworzenie pliku
filename = 'eob_bg_{p}.csv'.format(p=data)
f = open(filename, 'w', encoding='utf-8')


# naglowki
headers = " Nazwa; Cena \n"
f.write(headers)


kategorie = [[0,1,2, 3, 4, 5],["Mężczyźni","Kobiety","Dzieci", "Sport", "Akcesoria", "Torebki"],["https://www.obuvki.bg/m-zhki.html?p=1","https://www.obuvki.bg/damski.html?p=1","https://www.obuvki.bg/detski.html?p=1", "https://www.obuvki.bg/sport.html?p=1", "https://www.obuvki.bg/aksesoari.html?p=1", "https://www.obuvki.bg/chanti.html?p=1"]]

for line in kategorie[0]:
    my_url = kategorie[2][line]


    # opening website, grabing
    uClient = uReq(Req(my_url, headers={'User-Agent': 'Mozilla/5.0'}))
    page_html = uClient.read()
    uClient.close()
    # html parsing
    page_soup = soup(page_html, 'html.parser')
    
    # podanie ilosci stron
    ilosc_stron1 = page_soup.find("div", {"class": "toolbar-top__right-range"}).text
    ilosc_stron = ilosc_stron1.replace("z", "").replace("\n", "").replace(" ", "")
    a= ilosc_stron.replace("of", "")
        
         
    for i in range(int(a)):
        my_url = my_url
        uClient = uReq(Req(my_url, headers={'User-Agent': 'Mozilla/5.0'}))
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        buty = page_soup.findAll("li", {"class": "products-list__item"})
            
            
            
        for but in buty:
            nazwa = but.a["title"]            
            s_cena = but.find("div", {"class": "products-list__old-price"})
            s_cena = str(s_cena)[39:len(str(s_cena))-11]
            cena = but.find("div", {"class": "products-list__special-price"})
            cena = str(cena)[43:len(str(cena))-17]
            r_cena = but.find("div", {"class": "products-list__regular-price"})
            r_cena = str(r_cena)[43:len(str(r_cena))-11]
            
            if cena == "":
                cena=r_cena
                if cena =="":
                    cena=s_cena
            
            f.write(str(nazwa) + ";" + str(cena) + ";" + "\n")
               
                    
           
            if kategorie[1][line] == "Mężczyźni":
                my_url = 'https://www.obuvki.bg/m-zhki.html?p={p:s}'.format(p=str(i + 2))
            else:
                if kategorie[1][line] == "Kobiety":
                    my_url = 'https://www.obuvki.bg/damski.html?p={p:s}'.format(p=str(i + 2))
                else:
                    if kategorie[1][line] == "Dzieci":
                        my_url = 'https://www.obuvki.bg/detski.html?p={p:s}'.format(p=str(i + 2))
                    else:
                        if kategorie[1][line] == "Sport":
                            my_url = 'https://www.obuvki.bg/sport.html?p={p:s}'.format(p=str(i + 2))
                        else:
                            if kategorie[1][line] == "Akcesoria":
                                my_url = 'https://www.obuvki.bg/aksesoari.html?p={p:s}'.format(p=str(i + 2))
                            else:
                                if kategorie[1][line] == "Torebki":
                                    my_url = 'https://www.obuvki.bg/chanti.html?p={p:s}'.format(p=str(i + 2))
                                else:
                                    print("Błąd")
       
         
f.close()
       