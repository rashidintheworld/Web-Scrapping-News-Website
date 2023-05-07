import requests
from bs4 import BeautifulSoup
import LinkModul

header = {"User-Agent": "Mozilla/5.0"}

for link in LinkModul.linkler():
    url = link
    r = requests.get(url,headers=header)
    soup = BeautifulSoup(r.content, "html.parser")

    elementler = soup.find("div",attrs = {"class" :"_2UJGH"})
    basliq = elementler.find("div",attrs = {"class" :"JwYux"}).h1.text
    file = open("xeberler.txt","a",encoding = "UTF-8")
    xeber_metni = elementler.find_all("p")
    print(basliq,"\n")
    file.write(basliq+"\n"*2)

    for xeber in xeber_metni:
        print(xeber.text)
        file.write(xeber.text+"\n")

    print(">>Ətraflı oxumaq üçün keçid edin  {}".format(link))
    file.write(">>Ətraflı oxumaq ücün keçid edin  {}".format(link)+"\n")

    print("-"*50)
    file.write("-"*50+"\n")
    file.close()
