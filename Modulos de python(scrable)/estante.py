from fichas import Ficha

class Estante:
    """ Crea la "mano" de cada jugador. Permite a los jugadores agregar, eliminar y reponer el número de fichas en su
    mano. """

    def __init__(self, bolsa):
        """Inicializa la mano del jugador. Toma la bolsa de la que vendrán las fichas de las manos como argumento."""
        self.mano = []
        self.bolsa = bolsa
        self.inicializar_mano()

    def agregar_a_la_mano(self):
        """Toma una ficha de la bolsa y lo agrega a la mano del jugador."""
        self.mano.append(self.bolsa.tomar_de_la_bolsa())

    def inicializar_mano(self):
        """Agrega las 7 fichas iniciales a la mano del jugador."""
        for i in range(7):
            self.agregar_a_la_mano()

    def get_mano_str(self):
        """Muestra el estante del usuario en forma de cadena."""
        return ", ".join(str(ficha.get_letra()) for ficha in self.mano)

    def get_mano_arr(self):
        """Devuelve la mano como un arreglo de instancias de ficha"""
        return self.mano

    def quitar_ficha_de_la_mano(self, ficha):
        """Elimina una ficha de la mano (por ejemplo, cuando se juega una ficha)."""
        self.mano.remove(ficha)

    def devolver_ficha_mano(self, ficha):
        """Retorna una ficha y la descarta de la mano."""
        indice = self.mano.index(ficha)
        auxFicha = self.mano[indice]  # busco la ficha y me la quedo
        self.mano.remove(ficha)  # descarto la ficha de la mano
        return auxFicha

    def cambiar_ficha(self, lista):
        """Devuelve una o varias fichas de la mano a la bolsa y repone la mano"""
        fichas_a_descartar = []  # fichas a delvolver a la bolsa
        for fichaN in lista:
            fichas_a_descartar.append(self.devolver_ficha_mano(fichaN))
        for fichaD in fichas_a_descartar:
            self.bolsa.devolver_ficha_a_la_bolsa(fichaD)
        self.reponer_mano()

    def get_mano_longitud(self):
        """Devuelve el número de fichas que quedan en la mano."""
        return len(self.mano)

    def reponer_mano(self):
        """Agrega fichas al estante después de un turno, de modo que el estante tendrá 7 fichas (suponiendo una
        cantidad adecuada de fichas en la bolsa). """
        while self.get_mano_longitud() < 7 and self.bolsa.obtener_fichas_restantes() > 0:
            self.agregar_a_la_mano()

# ---------------------------------SECCION DE PRUEBAS-------------------------------
"""
from bolsa import Bolsa
import random

estante = Estante(Bolsa())
print("cantidad de fichas en mano: " + str(estante.get_mano_longitud()))
print("esta es la mano del jugador")
print(estante.get_mano_str())
mano_mentira = estante.get_mano_arr()[0:7]
aux_ficha = []

for i in range(3):
    print(i)
    victima = random.choice(mano_mentira)
    aux_ficha.append(victima)
    mano_mentira.remove(victima)
estante.cambiar_ficha(aux_ficha)


# print("se juegan las siguientes fichas:")
# for i in range(3):
#     aux_ficha = random.choice(estante.get_mano_arr())
#     print(aux_ficha.get_letra())
#     estante.quitar_ficha_de_la_mano(aux_ficha)
#print("cantidad de fichas en mano despues de jugar: " + str(estante.get_mano_longitud()))
#print("esta es la mano actual del jugador ")
#print(estante.get_mano_str())
"""