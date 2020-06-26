from itertools import permutations
import pattern.text.es
'''este programa genera todas las combinaciones posibles con las letras que recibe en una lista'''

# clasificaciones posibles para adjetivos y verbos
TIPO = {'adj': ["AO", "JJ", "AQ", "DI", "DT"],

        'verb': ["VAG", "VBG", "VAI", "VAN", "MD", "VAS", "VMG", "VMI", "VB", "VMM", "VMN", "VMP", "VBN", "VMS",
                 "VSG",
                 "VSI", "VSN", "VSP", "VSS"]
        }

class Palabra:

    def clasifico(self,palabra, clasificacion):
        '''
        Función que recibe una palabra y verifica que sea aadjetivo o verbo
        :param palabra: es un string
        :param clasificacion: un diccionario que tiene las clasficaciones que busco
        :return: True si está dentro de la clasificación, False caso contrario
        '''



        s = (pattern.text.es.parse(palabra)).split() # genera 1 lista dentro de otra lista y esta en otra lista con las posibles palabras generadas.
        print("vemos el split")
        print(s)
        for cada in s:
            for c in cada:
                for tipo in clasificacion:
                    #print("la clasificacion que se busca es {}".format(tipo))
                    if c[1] in clasificacion[tipo]:
                        print(palabra + " es del tipo " + tipo)
                        return True

    def es_palabra(self,pal):
        '''
        Verifica si es una palabra válida
        :param pal: un string
        :return: True si es, False caso contrario
        '''
        if pal in pattern.text.es.lexicon: # Busca palabras que estan en el archivo lexicon
            # print(pal + " en lexicon ")
            if pal in pattern.text.es.spelling: # Realiza una correccion ortografica
                # print(pal + " en spelling ")
                return True
        return False


    def armo_palabra(self,letras_palabras):
        '''
        Armo las posibles combinaciones y permutaciones con una lista de letras recibidas
        :param letras_palabras: lista de letras
        :return: un conjunto con las palabras armadas
        '''
        letras = ''
        # for letra in letras_palabras:
        #    letras += entradas[letra]
        for letra in letras_palabras:
            letras += letra
        #print(letras)
        palabras = set()
        for i in range(2, len(letras) + 1): # como minimo tiene 2 letras.
            palabras.update((map("".join, permutations(letras, i))))
        #print("Imprimo la palabra generada")
        #print(palabras)
        return (palabras)


"""
MAIN() pruebo mis funciones segun como juega la maquina
"""
"""
p=Palabra()
#Ejemplo de uso con una lista de letras dada
lista_palabras = p.armo_palabra(["c", "a", "s", "s", "k", "a", "r"]) # es un objeto {} <class 'set'>
#print(lista_palabras.pop())
# clasifico con pattern
#lista palabras válidas dad una clasificación
palabras_adj_verb = [] # almacenara las palabras validas ya sean adetivos o verbos
#todas las palabras válidas posibles

palabras_validas = [] # validan palabras que existen y se las almacena
for pal in lista_palabras:
    if p.es_palabra(pal): # valida si es valida
        palabras_validas.append(pal)
        if p.clasifico(pal, TIPO):
            palabras_adj_verb.append(pal)
#print(palabras_adj_verb)
#print(palabras_validas)

## LLamo al usuario


palabraUsuario = set()
palabraUsuario.add("llanura") # tiene problemas con las ñ
palabras_validasu=[]
palabras_adj_verbu=[]
palabras_sustantivou=[]
for palusu in palabraUsuario:
    if p.es_palabra(palusu): # valida si es valida
        palabras_validasu.append(palusu)
        if p.clasifico(palusu, TIPO):
            palabras_adj_verbu.append(palusu)
        else:
            palabras_sustantivou.append(palusu)

#for i in palabras_sustantivou:
    #print(i+" es del tipo sustantivo")
#print("----------"*50)
#print(palabras_adj_verbu)
#print(palabras_validasu)
#print(palabras_sustantivou
"""