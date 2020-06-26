"""
Juego de Scrabble
Classes:
Ficha - realiza un seguimiento de la letra y el valor de la ficha
Estante - realiza un seguimiento de las fichas en el estante de letras de un jugador
Bolsa2 - realiza un seguimiento de las fichas restantes en la bolsa
Palabras - comprueba la validez de una palabra y su ubicación
Tablero - realiza un seguimiento de la ubicación de las fichas en el tablero
"""
from fichas import Ficha
from random import shuffle
#Realiza un seguimiento de la puntuación de cada Ficha de letras Y la cantidad.
LETRAS_CANTIDAD = {"A": 12,
                   "B": 2,
                   "C": 4,
                   "CH": 1,
                   "D": 5,
                   "E": 12,
                   "F": 1,
                   "G": 2,
                   "H": 2,
                   "I": 6,
                   "J": 1,
                   "L": 4,
                   "LL": 1,
                   "M": 2,
                   "N": 5,
                   "Ñ": 1,
                   "O": 9,
                   "P": 2,
                   "Q": 1,
                   "R": 5,
                   "RR": 1,
                   "S": 6,
                   "T": 4,
                   "U": 5,
                   "V": 1,
                   "X": 1,
                   "Y": 1,
                   "Z": 1,
                   "Comodin": 2
                   }

LETRAS_PUNTAJE = {"A": 1,
                  "B": 3,
                  "C": 3,
                  "CH": 5,
                  "D": 2,
                  "E": 1,
                  "F": 4,
                  "G": 2,
                  "H": 4,
                  "I": 1,
                  "J": 8,
                  "L": 1,
                  "LL": 8,
                  "M": 3,
                  "N": 1,
                  "Ñ": 8,
                  "O": 1,
                  "P": 3,
                  "Q": 5,
                  "R": 1,
                  "RR": 8,
                  "S": 1,
                  "T": 1,
                  "U": 1,
                  "V": 4,
                  "X": 8,
                  "Y": 4,
                  "Z": 10,
                  "Comodin": 0
                  }


class Bolsa:
    """Crea la bolsa de todas las fichas que estarán disponibles durante el juego. Contiene 98 letras y dos fichas en blanco. No toma argumentos para inicializar. """
    def __init__(self):
        """ Crea la bolsa llena de fichas del juego y llama al método initialize_bag (), que agrega las 100 fichas predeterminadas a la bolsa. No toma argumentos. """
        self.bolsa = []
        self.inicializar_bolsa()

#------------------METODOS PARA INICIALIZAR LA BOLSA-----------------------------------
    def agregar_a_la_bolsa(self, ficha, cantidad):
        """Agrega n cantidad de fichas de un tipo de letra a la bolsa"""
        for i in range(cantidad):
            self.bolsa.append(ficha)

    def inicializar_bolsa(self):
        """Agrega una cierta cantidad de una ficha a la bolsa. Toma una ficha y una cantidad entera como argumentos."""
        global LETRAS_CANTIDAD
        global LETRAS_PUNTAJE
        for letra in LETRAS_PUNTAJE.keys():
            #parametros (LETRA ,   DICCIONARIO CON PUNTAJE ,   CANTIDAD DE FICHAS PARA ESA LETRA)
            self.agregar_a_la_bolsa(Ficha(letra,LETRAS_PUNTAJE),LETRAS_CANTIDAD[letra])
        shuffle(self.bolsa) #mezcla las fichas en la bolsa

#--------------------------------INTERFAZ PARA COMUNICARSE CON LA BOLSA-------------------------------------------

    def tomar_de_la_bolsa(self):
        """Elimina una ficha de la bolsa y se lo devuelve al usuario. Esto se utiliza para reponer el estante."""
        return self.bolsa.pop()

    def devolver_ficha_a_la_bolsa(self,ficha):
        """Agrega una ficha a la bolsa"""
        self.bolsa.append(ficha)
        shuffle(self.bolsa)  # mezcla las fichas en la bolsa

    def obtener_fichas_restantes(self):
        #Devuelve el número de fichas que quedan en la bolsa.
        return len(self.bolsa)
"""
#---------------------------------SECCION DE PRUEBAS-------------------------------
bolsa = Bolsa()
lista_jugador =[]
print("las fichas restantes en la bolsa son: "+str(bolsa.obtener_fichas_restantes()))
#--------------------------SIMULACION DEL JUEGO--------------------------------------------
print("Acontinuacion se tomaran 7 fichas")
for i in range(7):
    lista_jugador.append(bolsa.tomar_de_la_bolsa())
print("se tomaron las siguientes fichas: ")
for ficha_jugador in lista_jugador:
    print("letra: "+ficha_jugador.get_letra()+" puntaje: "+str(ficha_jugador.get_puntaje()))

print("Quedan {} en la bolsa".format(bolsa.obtener_fichas_restantes()))
"""