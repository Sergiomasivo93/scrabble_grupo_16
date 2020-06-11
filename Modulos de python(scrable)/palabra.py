from pattern.es import *
from pattern.web import Wiktionary

w = Wiktionary(language="es")

palabra = input("Ingrese la palabra a evaluar : ")

analisis = parse(palabra).split('/')  # Parsear es resolver una palabra o una oracion en las partes que los componen y describe sus roles sintacticos.

#print(analisis)

if analisis[1] == "JJ" or analisis[1] == "VB":
    print("es un verbo o un adjetivo")
    pass
elif (analisis[1] == "NN"):  # Es sustantivo
    article=w.search(palabra) #Busco la supuesta palabra en el Wiktionary
    print("es un sustantivo" if article!=None else "la palabra no existe")
else:
    print('la palabra no existe')