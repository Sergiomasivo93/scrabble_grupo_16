from bolsa import Bolsa
from jugador import Jugador
from tablero_fran import Tablero
from palabra import Palabra


class Juego:

    def __init__(self):
        self.bolsa = Bolsa()
        self.jugador = Jugador(self.bolsa)
        self.jugador.set_nombre("Teemo")  # solo para realizar el test
        self.maquina = Jugador(self.bolsa)
        self.maquina.set_nombre("Rinfo")  # solo para realizar el test
        self.tablero = Tablero()
        self.palabra = Palabra()

    def calcular_puntaje(self,fichas = []):
        """Dada una cantidad de fichas jugadas suponiendo que es una palabra valida acumula el puntaje de cada ficha
            NOTA: todavia no se contemplo el hecho de que la ficha pudo haberse colocado en un multiplicador
            (ver como conseguir el multiplicador asociado a la ficha)
        """
        count = 0
        for ficha in fichas:
            count += ficha.get_puntaje()
        return count


    def actualizar_estado(self):
        """funcion que retorna un dicccionario con los valores actualizados del model para poder actualizar la vista
           param:  Ninguno
           return: dic_estado {}

           Keys del diccionario:
            "estado_puntaje_jugador": puntaje actual del jugador
            "estado_puntaje_maquina": puntaje actual de la maquina
            "estado_bolsa": cantidad de fichas disponibles en la bolsa
            "estado_mano_jugador": lista de string's (fichas en la mano del jugador)
            "estado_mano_maquina": lista de string's (fichas en la mano la maquina)
        """
        dic_estado = {
            "estado_puntaje_jugador": self.jugador.get_puntaje(),
            "estado_puntaje_maquina": self.maquina.get_puntaje(),
            "estado_bolsa": self.bolsa.obtener_fichas_restantes(),
            "estado_mano_jugador":self.jugador.get_estante().get_mano_list_letras(),
            "estado_mano_maquina":self.maquina.get_estante().get_mano_list_letras()
        }
        return dic_estado

#-----------------------prueba de funcionalidades del juego--------------------------------
import random
juego = Juego()
estado = juego.actualizar_estado()
#esto es para poder probar el contador
fichas_jugadas_j = []
fichas_jugadas_m = []

print(estado)
for i in range(5):
    #accion del jugador
    ficha_j = random.choice(juego.jugador.get_estante().get_mano_arr())
    fichas_jugadas_j.append(ficha_j)
    juego.jugador.get_estante().quitar_ficha_de_la_mano(ficha_j)
    #accion de la maquina
    ficha_m = random.choice(juego.maquina.get_estante().get_mano_arr())
    fichas_jugadas_m.append(ficha_m)
    juego.maquina.get_estante().quitar_ficha_de_la_mano(ficha_m)

estado = juego.actualizar_estado()
print(estado)
#simulando que las fichas jugadas son palabras validas y suman puntaje a los jugadores
juego.jugador.incrementar_puntaje(juego.calcular_puntaje(fichas_jugadas_j))
juego.maquina.incrementar_puntaje(juego.calcular_puntaje(fichas_jugadas_m))

#reponiendo mano
juego.jugador.get_estante().reponer_mano()
juego.maquina.get_estante().reponer_mano()

estado = juego.actualizar_estado()
print(estado)