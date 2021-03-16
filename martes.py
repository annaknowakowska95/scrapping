

import time
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

czas = time.localtime()
data = str(str(czas[0])+"_"+str(czas[1])+"_"+str(czas[2]))


# tworzenie pliku
filename = 'martes_{p}.csv'.format(p=data)
f = open(filename, 'w')


# naglowki
headers = " Nazwa; Cena \n"
f.write(headers)


kategorie = [[0,1,2, 3, 4, 5],["Mężczyźni","Kobiety","Junior", "Sport", "Końcówki", "Wyprzedaże"],["https://www.sklepmartes.pl/6-mezczyzna?p=1","https://www.sklepmartes.pl/41-kobieta?p=1","https://www.sklepmartes.pl/76-junior?p=1", "https://www.sklepmartes.pl/118-sporty?p=1", "https://www.sklepmartes.pl/459-koncowki-serii?p=1", "https://www.sklepmartes.pl/1010-wyprzedaze?p=1"]]

for line in kategorie[0]:
    my_url = kategorie[2][line]


    # opening website, grabing
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    # html parsing
    page_soup = soup(page_html, 'html.parser')
    
    # podanie ilosci stron
    ilosc_stron1 = page_soup.find("div", {"class": "pager"}).text
    ilosc_stron = ilosc_stron1[len(ilosc_stron1)-13:]
    a= ilosc_stron[:2]
        
         
    for i in range(int(a)):
        my_url = my_url
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        buty = page_soup.findAll("li", {"class": "product-list__item"})
            
            
            
        for but in buty:
            nazwa = but.a.find("h3", {"itemprop": "name"}).text   
            cena = but.a.find("div", {"style": "display: none;"}).text
            cena = cena.replace("\n\n","").replace("\n"," ").replace(".",",")
            cena=cena.split(" ")
           
            try:
                f.write(str(nazwa) + ";" + str(cena[1]) + "\n")
            except UnicodeEncodeError:
                f.write("Błąd" + ";" + "Błąd" + ";" + "\n")    
                    
           
            if kategorie[1][line] == "Mężczyźni":
                my_url = 'https://www.sklepmartes.pl/6-mezczyzna?p={p:s}'.format(p=str(i + 2))
            else:
                if kategorie[1][line] == "Kobiety":
                    my_url = 'https://www.sklepmartes.pl/41-kobieta?p={p:s}'.format(p=str(i + 2))
                else:
                    if kategorie[1][line] == "Junior":
                        my_url = 'https://www.sklepmartes.pl/76-junior?p={p:s}'.format(p=str(i + 2))
                    else:
                        if kategorie[1][line] == "Sport":
                            my_url = 'https://www.sklepmartes.pl/118-sporty?p={p:s}'.format(p=str(i + 2))
                        else:
                            if kategorie[1][line] == "Końcówki":
                                my_url = 'https://www.sklepmartes.pl/459-koncowki-serii?p={p:s}'.format(p=str(i + 2))
                            else:
                                if kategorie[1][line] == "Wyprzedaże":
                                    my_url = 'https://www.sklepmartes.pl/1010-wyprzedaze?p={p:s}'.format(p=str(i + 2))
                                else:
                                    print("Błąd")
       
         
f.close()
       