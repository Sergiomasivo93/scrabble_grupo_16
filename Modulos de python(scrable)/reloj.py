import PySimpleGUI as sg
import datetime
import time

sg.change_look_and_feel('Black')

layout = [
    [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='-OUTPUT-')],
    [sg.Button('Pausa', key='button', button_color=('white', '#001480')),
     sg.Button('Reiniciar', button_color=('white', '#007339'), key='Reiniciar'),
     sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]
]

window = sg.Window('Window that stays open').layout(layout)

# ------------------------------VARIABLES GLOBALES-------------------------------------------------------------

counter = 0
minutos = 0
segundos= 0
mili_segundos = 0
paused = False
start_time = int(round(time.time() * 100))


# ------------------------------FUNCIONES-------------------------------------------------------------
def actualizar_tiempo():
    global counter,minutos,segundos,mili_segundos
    counter = int(round(time.time() * 100)) - start_time
    minutos = (counter // 100) // 60
    segundos = (counter // 100) % 60
    mili_segundos = counter % 100
    window['-OUTPUT-'].update('{:02d}:{:02d}.{:02d}'.format(minutos,segundos,mili_segundos))


# ------------------------------PRUEBAS---------------------------------------------------------------

while True:

    # --------- Leer y actualizar la ventana --------
    if not paused:
        event, values = window.read(timeout=10)
        actualizar_tiempo()
    else:
        event, values = window.read()
    if event == 'button':
        event = window[event].GetText()

    # --------- Hacer operaciones de botones --------
    if event == sg.WIN_CLOSED or event == 'Exit':  # ALWAYS give a way out of program
        break
    if event is 'Reiniciar':
        start_time = int(round(time.time() * 100))
        counter = 0
        paused_time = start_time
        actualizar_tiempo()
    elif event == 'Pausa':
        paused = True
        paused_time = int(round(time.time() * 100))
        element = window['button']
        element.update(text='Continuar')
    elif event == 'Continuar':
        paused = False
        start_time = start_time + int(round(time.time() * 100)) - paused_time
        element = window['button']
        element.update(text='Pausa')
    # --------- condicion para cortar el timer --------
    elif segundos == 5:
        paused = True
        paused_time = int(round(time.time() * 100))
        element = window['button']
        element.update(text='Continuar')

window.Close()
