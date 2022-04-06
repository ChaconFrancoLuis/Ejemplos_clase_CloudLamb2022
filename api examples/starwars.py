import pprint
import requests
import json

def swapi():
    l= "https://swapi.dev/api/"
    data = requests.get(l)
    tt = json.loads(data.text)
    lista= [key for key in tt]
    print(type(tt))
    print("\nBienvenido\nLas categorias son: \n")
    for i in lista:
        print(i,"\n")
    ciclo= True
    while ciclo:
      ask = input("escoge una categoria correcta:  ")
      for i in lista: 
          if ask == i:
             ciclo = False
             break
    f = 'https://swapi.dev/api/{}'.format(ask)
    data = requests.get(f)
    tt = json.loads(data.text)
    print(type(tt))
    pprint.pprint(tt)

swapi()
c= True
while c:
   con = str (input("\n precione cualquir tecla para comtinuar con otra categoria\n presione 'quit' o 'q' para salir: "))
   if con == "q" or con == "quit":
       c= False
       break
   swapi()