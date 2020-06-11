import PySimpleGUI as sg
import time



sg.ChangeLookAndFeel('DarkAmber')

fecha=time.strftime("%d/%m /%y")
dicPuntaje = {  fecha: 1  }

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

def generar_lista_listbox(dicPuntaje):
    lista_puntaje_default=[]
    #genero la lista para actualizar la vista del listbox
    for aux in dicPuntaje.keys():
        lista_puntaje_default.append(f"{aux}               {dicPuntaje[aux]}")
    return lista_puntaje_default

def actualizar_puntaje(dicPuntaje,puntaje,letras=""):
    listAux=letras.split(',')
    for letra in listAux:
        dicPuntaje[letra]=int(puntaje)

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------


listaPuntajeDefault = generar_lista_listbox(dicPuntaje)



layout = [
[sg.Text('Lista de puntajes', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Fecha \t Puntaje', font=("", 15))],
    [sg.Listbox(values=listaPuntajeDefault, size=(60, 6), key='listbox')]
    ]


window = sg.Window('Everything bagel', layout, default_element_size=(40, 1), grab_anywhere=False)

casa="hola"

while True:
    event, values = window.read()

    print(f"Evento: {event}")
    if event in (None, 'Exit'):
        break
    if(casa=="hola"):
        actualizar_puntaje(dicPuntaje,"20/6/20" ,"600" )
        listaPuntajeDefault = generar_lista_listbox(dicPuntaje)
        window['listbox'].update(values=listaPuntajeDefault)
        print(f"Evento: {values['letras']} ")
        print(f"Evento: {values['puntaje']}")
        casa="jojo"