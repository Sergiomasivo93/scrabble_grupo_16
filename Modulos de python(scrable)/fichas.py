class Ficha:
    """
   Clase que permite la creación de una ficha.
   Inicializa usando una cadena en mayúscula de una letra, y un número entero que representa la puntuación de esa letra.
    """
    def __init__(self, letra, letra_valor):
        """
        @parametros (String,Dic{})
        Inicializa la clase. Toma la letra como un string, y el diccionario
        """
        #Initializes the tile class. Takes the letter as a string, y el diccionario de valores de letras como argumento.
        self.letra = letra.upper()
        if self.letra in letra_valor:
            self.puntaje = letra_valor[self.letra]
        else:
            self.puntaje = 0

    def get_letra(self):
        """Retorna la letra de la ficha (string)."""
        return self.letra

    def get_puntaje(self):
        """Retorna el puntaje de la ficha"""
        return self.puntaje
