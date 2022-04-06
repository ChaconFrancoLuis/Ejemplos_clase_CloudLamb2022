from ast import If
import requests
import json


def chuck(): #definicion de una funcion llamada chuck
    categoria = r"http://api.icndb.com/categories" #Raw string (para evitar cualquier salto de linea)
    data = requests.get(categoria) #get request, read
    tt = json.loads(data.text)
    valor=tt["value"]
    print ("las categorias son:")
    for i in valor:
      print (i)
    ciclo= True
    while ciclo:
     ask =  str(input('\n selecione una categoria correcta: '))
     for i in valor: 
          if ask == i:
             ciclo = False
             break
    print(f"\n la categoria escogida fue: {ask}")       
    pagina = f"http://api.icndb.com/jokes/random?limitTo=[{ask}]" #Raw string (para evitar cualquier salto de linea)
    dato = requests.get(pagina) #get request, read
    print(type(dato)) 
    jl = json.loads(dato.text) #parsing json a python 
    ID = jl["value"]["id"]
    print(f"chiste ID:{ID}\n")
    print(jl["value"]["joke"],"\n")

chuck()

c= True
while c:
   con = str (input("\n precione cualquir tecla para comtinuar con mas chiste\n presione 'quit' o 'q' para salir: "))
   if con == "q" or con == "quit":
       c= False
       break
   chuck()