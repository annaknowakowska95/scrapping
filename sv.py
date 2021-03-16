# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 09:42:35 2021

@author: anowakowska
"""


import time
from urllib.request import urlopen as uReq, Request as Req
from bs4 import BeautifulSoup as soup

czas = time.localtime()
data = str(str(czas[0])+"_"+str(czas[1])+"_"+str(czas[2]))


# tworzenie pliku
filename = 'sv_bg_{p}.csv'.format(p=data)
f = open(filename, 'w', encoding='utf-8')


# naglowki
headers = " Nazwa; Marka; Cena; \n"
f.write(headers)


kategorie = [[0, 1, 2, 3, 4, 5],["m", "d", "s", "dz_s", "dz_b", "dz_u"],["https://www.sportvision.bg/produkti/mens/page-0", "https://www.sportvision.bg/produkti/womens/page-0", "https://www.sportvision.bg/produkti/page-0", "https://www.sportvision.bg/produkti/detsa/page-0", "https://www.sportvision.bg/obuvki/detsa/page-0", "https://www.sportvision.bg/drehi/detsa/page-0"]]

for line in kategorie[0]:
    my_url = kategorie[2][line]


    # opening website, grabing
    uClient = uReq(Req(my_url, headers={'User-Agent': 'Mozilla/5.0'}))
    page_html = uClient.read()
    uClient.close()
    # html parsing
    page_soup = soup(page_html, 'html.parser')
    
    
    
    # podanie ilosci stron
    a = page_soup.find("a", {"rel": "last"}).text
    
    
    
    
    for i in range(int(a)):
        my_url = my_url
        uClient = uReq(Req(my_url, headers={'User-Agent': 'Mozilla/5.0'}))
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        buty = page_soup.findAll("div", {"class": "wrapper-grid-view item product-item ease col-xs-6 col-sm-4 col-md-3 col-lg-3 grid-view"})
                
                
                
        for but in buty:
            nazwa = but["data-product-item-id"]    
            
            marka = but["data-productbrand"]
            
            cena = but["data-productprice"]
            
               
                
               
            f.write(str(nazwa) + ";" + str(marka) + ";" + str(cena) + ";" + "\n")
                   
                        
               
            if kategorie[1][line] == "m":
                my_url = 'https://www.sportvision.bg/produkti/mens/page-{p:s}'.format(p=str(i + 1))
            else:
                if kategorie[1][line] == "d":
                    my_url = 'https://www.sportvision.bg/produkti/womens/page-{p:s}'.format(p=str(i + 1))
                else:
                    if kategorie[1][line] == "s":
                        my_url = 'https://www.sportvision.bg/produkti/page-{p:s}'.format(p=str(i + 1))
                    else:
                        if kategorie[1][line] == "dz_s":
                            my_url = 'https://www.sportvision.bg/produkti/detsa/page-{p:s}'.format(p=str(i + 1))
                        else:
                            if kategorie[1][line] == "dz_b":
                                my_url = 'https://www.sportvision.bg/obuvki/detsa/page-{p:s}'.format(p=str(i + 1))
                            else:
                                if kategorie[1][line] == "dz_u":
                                    my_url = 'https://www.sportvision.bg/drehi/detsa/page-{p:s}'.format(p=str(i + 1))
                                else:
                                    print("Błąd")
           
         
f.close()
        

