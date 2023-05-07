import requests
from bs4 import BeautifulSoup
header = {"User-Agent":"Mozilla/5.0"}

def linkler():
    link_list = []
    url = "https://www.aznews.az/latest/"
    r = requests.get(url,headers=header)
    soup = BeautifulSoup(r.content,"html.parser")

    butun_linkler = soup.find_all("div",attrs={"class":"_1Cu9V"})

    for linkler in butun_linkler:
         link = linkler.a.get("href")
         link_list.append(link)
    return link_list

