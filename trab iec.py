from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
try:
    html = urlopen("https://store.steampowered.com/")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(),"html5lib")
    jogos = res.findAll("a", {"class":"tab_item "})

nome_jogos = []
preco_jogos = []
img_jogos = []
dados_jogos = []

for jogo in range(0,10):
    nome_jogos.append(jogos[jogo].findAll("div", {"class":"tab_item_name"}))
    preco_jogos.append(jogos[jogo].findAll("div", {"class":"discount_final_price"}))
    img_jogos.append(jogos[jogo].findAll("img", {"class":"tab_item_cap_img"}))

for jogo in range(0,10):
    nome_jogos[jogo] = str(nome_jogos[jogo][0])[27:len(nome_jogos[jogo])-7]
    preco_jogos[jogo] = str(preco_jogos[jogo][0])[34:len(preco_jogos[jogo])-7]
    img_jogos[jogo] = str(img_jogos[jogo][0])[35:len(img_jogos[jogo])-7]

print(" --------- Jogos mais populares da Steam ----------")
print("|                     Túlio Esaú                   |")
print("|                 Prof. Igor Peretta               |")
print("|                                                  |")

for item in range(0,10):
    print("| Nome: {} Preco: {}                               |\n".format(nome_jogos[item],preco_jogos[item]))
    print("| Link IMG: {}|\n".format(img_jogos[item]))
