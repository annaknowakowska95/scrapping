# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 12:12:40 2020

@author: anowakowska
"""



import time
from urllib.request import urlopen as uReq, Request as Req
from bs4 import BeautifulSoup as soup


czas = time.localtime()
data = str(str(czas[0])+"_"+str(czas[1])+"_"+str(czas[2]))

filename = 'ans_bg_{p}.csv'.format(p=data)
f = open(filename, 'w')


headers = "URL; strona; Nazwa; Cena; \n"
f.write(headers)


kategorie = [[0, 1, 2, 3],["Kobiety", "Mężczyźni", "Dziewczynki", "Chłopcy"],["https://answear.bg/k/tya?sort=date_desc&page=1", "https://answear.bg/k/toy?sort=date_desc&page=1", "https://answear.bg/k/momche?sort=popularity&page=1", "https://answear.bg/k/momiche?sort=popularity&page=1"]]

for line in kategorie[0]:
    my_url = kategorie[2][line]


    # opening website, grabing
    uClient = uReq(Req(my_url, headers={'User-Agent': 'Mozilla/5.0'}))
    page_html = uClient.read()
    uClient.close()
    # html parsing
    page_soup = soup(page_html, 'html.parser')
    
    # podanie ilosci stron
    ilosc_stron1 = page_soup.find("p", {"class": "Pager__pagerDetails__n_vzf"}).text
    a= int(ilosc_stron1[10:len(ilosc_stron1)-8])/80
        
         
    for i in range(int(a)):
        try:
            
            my_url = my_url
            uClient = uReq(Req(my_url, headers={'User-Agent': 'Mozilla/5.0'}))
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html, "html.parser")
            buty = page_soup.findAll("div", {"class": "col-md-4 col-lg-3 col-xs-6"})
            
                
                
                
            for but in buty:
                nazwa = but.a["href"]            
                cena = but.find("p", {"class": "Price__currentPrice__2--Sj"})
                cena = cena.text.replace("<p class=""Price__currentPrice__2--Sj Price__currentPrice--sale__1IYx2"">", "")
                cena = cena[0:len(cena)-4]
                cena = cena.replace(".", ",")
                
                
                try:
                    f.write(str(my_url) + ";" + str(i) + ";" + str(nazwa) + ";" + str(cena) + "\n")
                except UnicodeEncodeError:
                    print("Błąd")    
               
                if kategorie[1][line] == "Kobiety":
                    my_url = 'https://answear.bg/k/tya?sort=date_desc&page={p:s}'.format(p=str(i + 1))
                else:
                    if kategorie[1][line] == "Mężczyźni":
                        my_url = 'https://answear.bg/k/toy?sort=date_desc&page={p:s}'.format(p=str(i + 1))
                    else:
                        if kategorie[1][line] == "Dziewczynki":
                            my_url = 'https://answear.bg/k/momche?sort=popularity&page={p:s}'.format(p=str(i + 1))
                        else:
                            if kategorie[1][line] == "Chłopcy":
                                my_url = 'https://answear.bg/k/momiche?sort=popularity&page={p:s}'.format(p=str(i + 1))
                            else:
                                print("Błąd")
        except:
            break




f.close()
       