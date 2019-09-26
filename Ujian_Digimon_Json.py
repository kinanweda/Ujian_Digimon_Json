from bs4 import BeautifulSoup
import requests
import json

req = requests.get('http://digidb.io/digimon-list/')
soup = BeautifulSoup(req.content,'html.parser')
# print(soup.prettify())

data = soup.find('table', id='digiList')
# print(data)
data = data.find_all('tr')
digi = []
for i in data[1:]:
    no = i.td
    nama = i.a
    gambar = i.img['src']
    stage = i.center
    types = i.td.find_next_sibling().find_next_sibling().find_next_sibling()
    attribute = types.find_next_sibling()
    memory = attribute.find_next_sibling()
    equip = memory.find_next_sibling()
    hp = equip.find_next_sibling()
    sp = hp.find_next_sibling()
    atk = sp.find_next_sibling()
    defn = atk.find_next_sibling()
    intl = defn.find_next_sibling()
    spd = intl.find_next_sibling()
    dicts = {
        "No":int(no.string),
        "Nama" : nama.string,
        "Gambar" : gambar,
        "Stage" : stage.string,
        "Type" : types.string,
        "Attribute" : attribute.string,
        "Memory" : memory.string,
        "Equip" : equip.string,
        "HP":hp.string,
        "SP":sp.string,
        "ATK":atk.string,
        "DEF": defn.string,
        "INT":intl.string,
        "Speed":spd.string
    }
    digi.append(dicts)

#Save to Json
with open('digimon.json','w') as x :
    x.write(json.dumps(digi,indent=2))