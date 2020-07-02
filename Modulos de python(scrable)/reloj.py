import PySimpleGUI as sg

class Reloj():
    sg.change_look_and_feel('Black')
    counter = 0
    seg=0
    ts = True
    tm = True
    fin=True
    conts = 0
    contm = 0
    una = 1
    def dameLayout(self):
        layout = [
            sg.Text(' ', size=(28, 2), font=('Helvetica', 16), justification='center', key='reloj')]

        return layout;

    def darSegundo(self):

        if((self.counter // 100) % 60==30):
            self.conts+=1
        if(self.conts==1):
            self.ts=False
            return 30
        return 0
    #def TurnoDeComputadora(self): # el turno es de 30 segundos para el usuario
       # seg = r.darSegundo();
        #if( (seg == 30)and (r.finJuego())):
           # print("Es turno de la computadora")

    def darMinuto(self):
        if(((self.counter // 100) // 60)==1):
            self.contm += 1
        if (self.contm == 1 and self.tm == True):
            self.tm = False
            return 1
        return 0


    def finJuego(self): # Termina el juego cuando pasa 1 minuto
        min = self.darMinuto();
        if (min == 1):
            print("Fin del juego")
            return False
        else:
            return True

# Esto lo haria en el tablero_fran





"""

r=Reloj()
window = sg.Window('Window that stays open').layout(r.dameLayout())



while True:      
    event, values = window.read(timeout=10)
    # acualizar tiempo
    FinJuego=r.finJuego()
    if(FinJuego==True):
        #if(r.una==0):
         #   print("Hola")
        print("hola")
        if(r.una==1):
            window['reloj'].update(
            '{:02d}:{:02d}.{:02d}'.format((r.counter // 100) // 60, (r.counter // 100) % 60, r.counter % 100))
            print("chau")
    if (FinJuego == False):
        #print("entre al else")
        r.una = 0;
        window['reloj'].update(
        '01:00:00')

    r.counter += 1
    r.TurnoDeComputadora();
    j=FinJuego;

    #min=r.darMinuto();
    #if(min==1):
    #    print("1")
    if event is None or event == 'Exit':      
        break      

window.Close()



"""