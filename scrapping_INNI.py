import requests
from bs4 import BeautifulSoup
import json

url = "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INNI&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000"
r = requests.get(url)
r.encoding = "utf-8"

soup = BeautifulSoup(r.text, "html.parser")
tabla = soup.find_all("tr", style = "background-color:#e5e5e5;")
tabla2 = soup.find_all("tr", style = "background-color:#FFFFFF;")
lista=[]

for c in tabla:
    temp = []
    for a in c:
        temp.append(a)
    datos = {
        "NRC" : temp[1].text,
        "Clave" : temp[3].a.text,
        "Nombre" : temp[5].a.text,
        "Seccion" : temp[7].text,
        "Creditos" : temp[9].text,
        "Cupos" : temp[11].text,
        "Cupos disponibles" : temp[13].text,
        "Horario" : temp[15].text[5:14],
        "Dias" : temp[15].text[14:25],
        "Edificio" : temp[15].text[25:29],
        "Aula" : temp[15].text[29:33],
        "Periodo" : temp[15].text[33:52],
        "Profesor" : temp[17].text[4:-1],
    }
    lista.append(datos)

for c in tabla2:
    temp = []
    for a in c:
        temp.append(a)
    datos = {
        "NRC" : temp[1].text,
        "Clave" : temp[3].a.text,
        "Nombre" : temp[5].a.text,
        "Seccion" : temp[7].text,
        "Creditos" : temp[9].text,
        "Cupos" : temp[11].text,
        "Cupos disponibles" : temp[13].text,
        "Horario" : temp[15].text[5:14],
        "Dias" : temp[15].text[14:25],
        "Edificio" : temp[15].text[25:29],
        "Aula" : temp[15].text[29:33],
        "Periodo" : temp[15].text[33:52],
        "Profesor" : temp[17].text[4:-1],
    }
    lista.append(datos)


with open("oferta_INNI.json", "w") as archivo:
    json.dump(lista, archivo, sort_keys=False, indent=4)
#print(lista)
