from bolsa import Bolsa
from estante import Estante
from fichas import Ficha
from jugador import Jugador
from tablero_fran import Tablero
from palabra import Palabra
class Juego:
    bolsa=Bolsa() #inicializa la bolsa
    tablero=Tablero()
    palabra=Palabra()
    jugador=Jugador(bolsa)
    def initContexto(self):
        #self.bolsa.inicializar_bolsa()
        self.tablero.tableroConfig()
        self.jugador.set_nombre("Rodrigo")
        

    #def Jugar(self):
        #while(True):
            #si se cumplio el tiempoTotal o no puedo tomar fichas de la bolsa o se presiona terminar:
            #    break
            #turnoJugador()
            #turnoMaquina
            
    #def turnoJugador(self):
        #roboinicial (unica vez) o robo 7 la primera vez
        #robonormal (despues del 1er robo y si jugue fichas la vez pasada)
        #jugar
            #roba
        #cambiarLetras

    #def turnoMaquinaTerminator(self):
        #roboinicial
        #logica de la maquina (la ia)
juego=Juego()
juego.initContexto()
print(juego.jugador.get_estante().get_mano_arr().pop().get_letra())
