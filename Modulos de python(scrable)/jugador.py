from estante import Estante
from bolsa import Bolsa


class Jugador:
    """Crea una instancia de un jugador. Inicializa el estante del jugador y le permite configurar / obtener un
    nombre de jugador. """

    def __init__(self, bolsa):
        """Inicializa una instancia de jugador. Crea el estante del jugador creando una instancia de esa clase. Toma
        la bolsa como argumento para crear el estante. """

        self.nombre = ""
        self.estante = Estante(bolsa)
        self.puntaje = 0

    def set_nombre(self, nombre):
        """Establece el nombre del jugador."""
        self.nombre = nombre

    def get_nombre(self):
        """Obtiene el nombre del jugador."""
        return self.nombre

    def get_estante(self):
        """Devuelve el estante del jugador esto sirve para cuando se deben reponer fichas del jugador"""
        return self.estante

    def get_estante_str(self):
        """Devuelve el estante del jugador en forma de str."""
        return self.estante.get_mano_str()

    def get_estante_arr(self):
        """Devuelve el estante del jugador en forma de matriz."""
        return self.estante.get_mano_arr()

    def incrementar_puntaje(self, incrementar):
        """Aumenta la puntuación del jugador en una cierta cantidad. Toma el incrementar (int) como argumento y lo agrega
        a la puntuación. """
        self.puntaje += incrementar

    def get_puntaje(self):
        """Devuelve la puntuación del jugador"""
        return self.puntaje


#---------------------------------SECCION DE PRUEBAS-------------------------------
# import random
# jugador1 = Jugador(Bolsa())
# jugador1.set_nombre("Redux")
# maquina = Jugador(Bolsa())
# maquina.set_nombre("Carlitos")
# print("---------RONDA 1---------------")
# print("---------PUNTAJES---------------")
# print(jugador1.get_nombre()+"(Player): "+str(jugador1.get_puntaje()))
# print(maquina.get_nombre()+"(PC): "+str(maquina.get_puntaje()))
# print("---------SE JUEGAN FICHAS---------------")
# #obtengo el estante con 7 fichas de cada jugador
# estanteJ1 = jugador1.get_estante()
# estanteMQ = maquina.get_estante()
# print("las fichas del jugador son: "+estanteJ1.get_mano_str())
# print("las fichas del la maquina son: "+estanteMQ.get_mano_str())
# print("---------------------------------------------------------")
# print("---------------------------------------------------------")
# fichas_a_jugar = random.randint(0, 5)
# for i in range(fichas_a_jugar):
#     print("el jugador "+jugador1.get_nombre()+" juega una ficha")
#     auxFichaJugador = random.choice(estanteJ1.get_mano_arr())
#     estanteJ1.quitar_ficha_de_la_mano(auxFichaJugador)
# print(jugador1.get_nombre()+" le quedan: "+str(estanteJ1.get_mano_longitud())+" fichas en el estante")
# print("---------------------------------------------------------")
# print("---------------------------------------------------------")
# fichas_a_jugar = random.randint(0, 5)
# for j in range(fichas_a_jugar):
#     print("el jugador " + maquina.get_nombre() + " juega una ficha")
#     auxFichaMaquina = random.choice(estanteMQ.get_mano_arr())
#     estanteMQ.quitar_ficha_de_la_mano(auxFichaMaquina)
# print(maquina.get_nombre()+" le queda: "+str(estanteMQ.get_mano_longitud())+" fichas en el estante")
# print("---------------------------------------------------------")
# print("---------------------------------------------------------")
# print("Ahora ambos jugadores tienen pocas fichas")
# print("las fichas del jugador son: "+estanteJ1.get_mano_str())
# print("las fichas del la maquina son: "+estanteMQ.get_mano_str())
# print("---------------------------------------------------------")
# print("---------------------------------------------------------")
# print("Se van a reponer las fichas de los jugadores")
# estanteJ1.reponer_mano()
# estanteMQ.reponer_mano()
# print("---------------------------------------------------------")
# print("---------------------------------------------------------")
# print("Se han repuesto la cantidad de fichas de los jugadores")
# print("---------------------------------------------------------")
# print("las fichas del jugador son: "+estanteJ1.get_mano_str())
# print("las fichas del la maquina son: "+estanteMQ.get_mano_str())
# print("---------FIN DE LA RONDA 1---------------")