import PySimpleGUI as sg
from tablero import Tablero

ta = Tablero()

class Vista:
    sg.theme('Darkamber')  # declaracion del color
    def __init__(self):
        # ----------------------------------------------------------------------------
        # ------------------------ Estructura definicion ---------------------------------
        self.dicPuntaje = {"a": 1, "b": 3, "c": 2, "d": 2,
                           "e": 1, "f": 4, "g": 2, "h": 4,
                           "i": 1, "j": 6, "k": 8, "l": 1,
                           "m": 3, "n": 1, "o": 1, "p": 3,
                           "q": 8, "r": 1, "s": 1, "t": 1,
                           "u": 1, "v": 4, "w": 8, "x": 8,
                           "y": 4, "z": 10, "ñ": 8, }
        self.listaPuntajeDefault = self.generar_lista_listbox(self.dicPuntaje)
        self.nombreJ = "default"
        self.dic_estado = {} #variable para la comunicacion de datos del modelo con la vista(en particular ocn el tablero)
        #---------------------------------------------------------------------------
        #_-------------------------Tab definicion -----------------------------------
        self.tab1_layout = [
            [sg.T('Haga click en la pestaña Configuracion si decea modificar lo siguiente:')],
            [sg.T('\t Tiempo. \n \t Nivel. \n \t Puntaje para las letras. \n')],
            [sg.T('Haga click en la pestaña Historial si decea visualizar los puntajes obtenidos durante el juego.')],
            [sg.T('\n Haga click en el boton Comenzar si desea jugar.')],
            [sg.T('\n Antes de comenzar Ingrese su nombre.')],
            [sg.InputText('',pad=(10,0), size=(10, 1), tooltip='por ejemplo: pepe',key='nombre_jugador'),sg.Button('Establecer',key='Establecer')]
        ]
        self.tab2_layout = [
            [sg.Text('Configuracion para el juego', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
            [sg.Text('Duracion del juego (minutos)', font=("", 15))],
            [sg.InputCombo(('2', '5', '7', '10', '12', '15', '20'), readonly=True, text_color='dark', default_value=2, size=(3, 1), key='tiempo')],
            [sg.Frame(layout=[
                [sg.Radio('Facil', "RADIO1", default=True, font=("", 12), key='facil'),
                 sg.Radio('Medio', "RADIO1", font=("", 12), key='medio'),
                 sg.Radio('Dificil', "RADIO1", font=("", 12), key='dificil')]
            ],
                title='Niveles', title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='seleciona alguna opción',
                font=("", 15))
            ],
            [sg.Text('_' * 80)],
            # [sg.Text('Cargar configuracion', size=(35, 1))],
            # [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
            #  sg.InputText('Default Folder'), sg.FolderBrowse()],
            [sg.Text('Puntaje para las letras:', font=("", 15))],
            [sg.Text('Puntaje:', font=("", 12)),
             sg.InputCombo(('5', '10', '15'), readonly=True, default_value=5, text_color='dark', size=(10, 1),
                           key='puntaje'),
             sg.Text('Letras:', font=("", 12)),
             sg.InputText('', size=(10, 1), tooltip='introduzca letras separados por "," por ejemplo: a,b,c',
                          key='letras'),
             sg.Button('Modificar')],
            [sg.Text('_' * 80)],
            [sg.Text('Letras con sus puntajes:')],
            [sg.Text('_' * 80)],
            [sg.Listbox(values=self.listaPuntajeDefault, size=(60, 6), key='listbox')],
            # [sg.Submit(tooltip='Haz click en guardar'), sg.Cancel()]
            [sg.Button('Guardar')]
        ]
        self.tab3_layout = [[sg.T('Aca esta el historial que esta hecho en el historial.py:')]]
        # ----------------------------------------------------------------------------
        # ------------------------ Columna definicion ---------------------------------
        self.column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],
                   [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
                   [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
                   [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]
        # ----------------------------------------------------------------------------
        # ------------------------ Layout definicion ---------------------------------
        self.layout = [
            [sg.TabGroup([[sg.Tab('Inicio', self.tab1_layout), sg.Tab('Configuracion', self.tab2_layout), sg.Tab('Historial', self.tab3_layout)]])],
            [sg.Button('Comenzar',key='Comenzar',disabled=True), sg.Button('Salir')]
        ]
        self.window = sg.Window('Everything bagel', self.layout, default_element_size=(40, 1), grab_anywhere=False)

    # ----------------------------FUNCIONES-----------------------------------
    # ----------------------------------------------------------------------------
    def get_nombreJ(self):
        """retorna el nombre para el jugador (introducido desde el menu de inicio)"""
        return self.nombreJ
    def get_dic_estado(self):
        """
           funcion que retorna un diccionario que contiene los valores que se visualizan
           esta variable sirve de intermediario para manipular el controlador
        """
        return self.dic_estado
    def set_dic_estado(self,dic_estado):
        """
        sirve para establecer en la vista los valores que recibira del modelo
        """
        self.dic_estado = dic_estado

    def generar_lista_listbox(self, dicPuntaje):
        lista_puntaje_default = []
        # genero la lista para actualizar la vista del listbox
        for aux in dicPuntaje.keys():
            lista_puntaje_default.append(f"{aux} = {dicPuntaje[aux]}")
        return lista_puntaje_default

    def actualizar_puntaje(self, dicPuntaje, puntaje, letras=""):
        listAux = letras.split(',')
        for letra in listAux:
            dicPuntaje[letra] = int(puntaje)

    def correr_ventana(self ,juego):
        while True:
            event, values = self.window.read()
            print(f"Evento: {event}")
            if event is None or event == 'Salir':  # always,  always give a way out!
                break
            if event == 'Establecer':
                self.nombreJ = values['nombre_jugador']
                juego.set_nombre_J(self.nombreJ)

                self.window['Comenzar'].update(disabled=False)
            if event == 'Comenzar':
                ta.cargar_datos_vista(juego.actualizar_estado())
                ta.ejecutarTablero()
            if event in (None, 'Exit'):
                break
            if event in ('Modificar'):
                if (values['puntaje'] != "" and values['letras'] != ""):
                    l = values['letras'].split(",")  # lista de las letras que escribo en el text
                    # print(l) verificar que imprime
                    for i in l:
                        if (i in self.dicPuntaje.keys()):
                            self.actualizar_puntaje(self.dicPuntaje, values['puntaje'], values['letras'])
                            self.listaPuntajeDefault = self.generar_lista_listbox(self.dicPuntaje)
                            self.window['listbox'].update(values=self.listaPuntajeDefault)
                            print(f"Evento: {values['letras']}")
                            print(f"Evento: {values['puntaje']}")

            if event in ('Guardar'):  # cuando presiono guardar me guardo lo siguiente
                # El estado del juego
                if (values['facil'] == True):
                    niveles = "facil"
                if (values['medio'] == True):
                    niveles = "medio"
                if (values['dificil'] == True):
                    niveles = "dificil"
                # El tiempo del juego

                num = int(values['tiempo'])  # es un string --> lo casteo  a int
                # cuenta=num*60 #convierto a segundos
                # El diccionario que posee las letras con los puntajes cambiados que esta en dicPuntaje
                sg.popup('Se guardo lo siguiente',
                         '',
                         'Nivel= {}'.format(niveles),
                         'Tiempo= {}'.format(num),
                         'Puntajes de cada letra= ',
                         "\n".join("{}=  {}".format(k, v) for k, v in self.dicPuntaje.items()),
                         )
        self.window.close()

#--------------------------Test de la clase vista(ventana)-------------------------------------------
# v = Vista()
# v.correr_ventana()
#nota hace falta una forma de que se le puedan pasar datos des jugador desde la vista al modelo y desde el modelo a la vista
