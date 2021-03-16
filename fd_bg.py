# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 14:56:01 2021

@author: anowakowska
"""

import time
from urllib.request import urlopen as uReq, Request as Req
from bs4 import BeautifulSoup as soup

czas = time.localtime()
data = str(str(czas[0])+"_"+str(czas[1])+"_"+str(czas[2]))


# tworzenie pliku
filename = 'fd_bg_{p}.csv'.format(p=data)
f = open(filename, 'w', encoding='utf-8')


# naglowki
headers = " Nazwa; Cena \n"
f.write(headers)


kategorie = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],["d_o", "d_b", "d_a", "d_s", "d_p", "m_o", "m_b", "m_a", "m_s", "m_p", "dz_o", "dz_b", "ch_o", "ch_b"],["https://www.fashiondays.bg/s/new-in-menu-mmse-w?page=1", "https://www.fashiondays.bg/s/shoes-menu-mmse-w?page=1", "https://www.fashiondays.bg/s/acc-new-in-menu-mmse-w?page=1", "https://www.fashiondays.bg/s/sport-brands-menu-mmse-w?page=1", "https://www.fashiondays.bg/s/premium-brands-menu-mmse-w?page=1", "https://www.fashiondays.bg/g/%D0%9C%D1%8A%D0%B6%D0%B5-/%D0%94%D1%80%D0%B5%D1%85%D0%B8?page=1", "https://www.fashiondays.bg/g/%D0%9C%D1%8A%D0%B6%D0%B5-/%D0%9E%D0%B1%D1%83%D0%B2%D0%BA%D0%B8?page=1", "https://www.fashiondays.bg/s/acc-new-in-menu-mmse-m?page=1", "https://www.fashiondays.bg/s/sport-brands-menu-mmse-m?page=1", "https://www.fashiondays.bg/s/premium-brands-menu-mmse-m?page=1", "https://www.fashiondays.bg/s/new-in-menu-g?page=1", "https://www.fashiondays.bg/s/new-in-footwear-menu-g", "https://www.fashiondays.bg/s/new-in-menu-b?page=1", "https://www.fashiondays.bg/s/new-in-footwear-menu-b"]]

for line in kategorie[0]:
    my_url = kategorie[2][line]


    # opening website, grabing
    uClient = uReq(Req(my_url, headers={'User-Agent': 'Mozilla/5.0'}))
    page_html = uClient.read()
    uClient.close()
    # html parsing
    page_soup = soup(page_html, 'html.parser')
    
    
    
    if kategorie[1][line] == "dz_b" or kategorie[1][line] == "ch_b":
        a=1
    else:
    
        # podanie ilosci stron
        a = page_soup.find("a", {"class": "paginationLink paginationLastPage"}).text
        
           
             
        for i in range(int(a)):
            my_url = my_url
            uClient = uReq(Req(my_url, headers={'User-Agent': 'Mozilla/5.0'}))
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html, "html.parser")
            buty = page_soup.findAll("li", {"class": "col-xs-6 col-sm-4 col-md-4 col-lg-4 vrecom_product"})
                
                
                
            for but in buty:
                nazwa = but.a["data-gtm-sku"]    
                print(nazwa)
                cena = but.a["data-gtm-price"]
                print(cena)
               
                
               
                f.write(str(nazwa) + ";" + str(cena) + ";" + "\n")
                   
                        
               
                if kategorie[1][line] == "d_o":
                    my_url = 'https://www.fashiondays.bg/s/new-in-menu-mmse-w?page={p:s}'.format(p=str(i + 2))
                else:
                    if kategorie[1][line] == "d_b":
                        my_url = 'https://www.fashiondays.bg/s/shoes-menu-mmse-w?page={p:s}'.format(p=str(i + 2))
                    else:
                        if kategorie[1][line] == "d_a":
                            my_url = 'https://www.fashiondays.bg/s/acc-new-in-menu-mmse-w?page={p:s}'.format(p=str(i + 2))
                        else:
                            if kategorie[1][line] == "d_s":
                                my_url = 'https://www.fashiondays.bg/s/sport-brands-menu-mmse-w?page={p:s}'.format(p=str(i + 2))
                            else:
                                if kategorie[1][line] == "d_p":
                                    my_url = 'https://www.fashiondays.bg/s/premium-brands-menu-mmse-w?page={p:s}'.format(p=str(i + 2))
                                else:
                                    if kategorie[1][line] == "m_o":
                                        my_url = 'https://www.fashiondays.bg/g/%D0%9C%D1%8A%D0%B6%D0%B5-/%D0%94%D1%80%D0%B5%D1%85%D0%B8?page={p:s}'.format(p=str(i + 2))
                                    else:
                                        if kategorie[1][line] == "m_b":
                                            my_url = 'https://www.fashiondays.bg/g/%D0%9C%D1%8A%D0%B6%D0%B5-/%D0%9E%D0%B1%D1%83%D0%B2%D0%BA%D0%B8?page={p:s}'.format(p=str(i + 2))
                                        else:
                                            if kategorie[1][line] == "m_a":
                                                my_url = 'https://www.fashiondays.bg/s/acc-new-in-menu-mmse-m?page={p:s}'.format(p=str(i + 2))
                                            else:
                                                if kategorie[1][line] == "m_s":
                                                    my_url = 'https://www.fashiondays.bg/s/sport-brands-menu-mmse-m?page={p:s}'.format(p=str(i + 2))
                                                else:
                                                    if kategorie[1][line] == "m_p":
                                                        my_url = 'https://www.fashiondays.bg/s/premium-brands-menu-mmse-m?page={p:s}'.format(p=str(i + 2))
                                                    else:
                                                        if kategorie[1][line] == "dz_o":
                                                            my_url = 'https://www.fashiondays.bg/s/new-in-menu-g?page={p:s}'.format(p=str(i + 2))
                                                        else:
                                                            if kategorie[1][line] == "dz_b":
                                                                my_url = 'https://www.fashiondays.bg/s/new-in-footwear-menu-g'
                                                            else:
                                                                if kategorie[1][line] == "ch_o":
                                                                    my_url = 'https://www.fashiondays.bg/s/new-in-menu-b?page={p:s}'.format(p=str(i + 2))
                                                                else:
                                                                    if kategorie[1][line] == "ch_b":
                                                                        my_url = 'https://www.fashiondays.bg/s/new-in-footwear-menu-b'
                                                                    else:
                                                                        print("Błąd")
           
         
f.close()
        
      
