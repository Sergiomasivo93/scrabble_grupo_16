import PySimpleGUI as sg
from reloj import Reloj as re
class Tablero:
    tam_celda=0
    #-------Variables para inicio y manejo del tablero-----------------------------
    matriz = []             #matriz de dibujo
    selected = []           #matriz que guarda si seleccione a un boton 
    text_box = []           #matriz q guarda las letras
    matriz_puntaje=[]       #matriz q guarda las casillas con puntajes especiales
    #------------------------------------------------------------------------------
    casillas_palabra_x3=[]  
    casillas_palabra_x2=[]
    casillas_letra_x3=[]
    casillas_letra_x2=[]
    casillas_letra_resto1=[]
    casillas_letra_resto2=[]
    casillas_letra_resto3=[]
    tablero = None
    diccionario_colores={"Rojo":"#ea3232","Azul":"#4b7eea","Verde":"#50ea4b","Amarillo":"#c4bc00","Rosado":"#fd73f0","Naranja":"#fb981e","Marron":"#b46708"}
    
    boton_seleccionado=False
    boton_actual=None
    letraActual="1erLetra"
    pos1erLetraX=0
    pos1erLetraY=0
    pos2daLetraX=0
    pos2daLetraY=0
    sentido="" #Horizontal o vertical
    listaPos=[]
    cortaTodo=False
    r = re()
    def botonConfig(self, texto):
        #funciona
        color_button = ('white', 'green') #primer parametro:color de letra, segundo parametro: color fondo
        tam_button = 4, 0
        return sg.Button(texto, button_color=color_button, size=tam_button)
    def initVariables(self):
        self.tam_celda = 25
        for i in range(0, 15):
            self.matriz.append([0] * 15)
            self.selected.append([False] * 15)
            self.text_box.append([""] * 15)
            self.matriz_puntaje.append([""] * 15)
    def tableroConfig(self):
        #tamaño del canvas en pixeles
        self.initVariables()
        tamaño=(550,500) #tamaño total del canvas
        esquina_inferior_izquierda=(0,385) #tamaño que depende del tamaño de celda*cantidad de celdas 
        esquina_superior_derecha=(385,0)   #tamaño que depende del tamaño de celda*cantidad de celdas
        #esquina_inferior_izquierda y esquina_superior_derecha marcan hasta donde se dibuja el tablero.
        #Esto seria q va desde x=0 hasta x=385 y y=0 hasta y=385
        return sg.Graph(tamaño, esquina_inferior_izquierda, esquina_superior_derecha, key='_GRAPH_', background_color='white', change_submits=True,
              drag_submits=False)
            
    def coordenadasColor(self):
        #(x,y)
        self.casillas_palabra_x3=[(0,0), (0,7), (0,14), (7,0), (7,7), (7,14), (14,0), (14,7), (14,14)] #Rojo- Palabrax3
        self.casillas_palabra_x2=[(1,1), (3,3), (11,11), (13,13), (13,1), (11,3), (3,11), (1,13)] #Azul - Palabrax2
        self.casillas_letra_x3=[(1,5), (1,9), (5,1), (5,13), (9,1), (9,13), (13,5), (13,9)] #Amarillo - Letrax3
        self.casillas_letra_x2=[(0,3), (0,11), (3,0), (3,7), (3,14), (6,6), (6,8), (7,3), (7,11), (8,6), (8,8), (11,0), (11,7), (11,14), (14,3), (14,11)] #Verde - Letrax2
        self.casillas_letra_resto1=[(2,2),(4,4),(10,10),(12,12),(12,2),(10,4),(4,10),(2,12)] #Rosado - Resto1
        self.casillas_letra_resto2=[(2,6), (2,8), (8,2),(12,6), (12,8), (6,2), (6,12), (8,12)]  #Naranja - Resto2
        self.casillas_letra_resto3=[(5,5), (5,9), (9,5), (9,9)] #Marron - Resto3
    
    def dibujarTablero(self, matriz,lista_letras):
        colorear_canvas= lambda x, y, z: g.TKCanvas.itemconfig(self.matriz[x][y], fill=z) #Colorea casilleros especiales
        boton=lambda texto:self.botonConfig(texto)
        tablero=self.tableroConfig()
        self.coordenadasColor()
        #------------Esto de aca abajo seria el estante, despues ver si lo sacamos o que onda
         # FILA
        pc = [boton(texto) for texto in lista_letras]  # estante del jugador(interfaz)
        player = [boton(texto) for texto in lista_letras]
        # COLUMNA
        nombre = "NombreJugador"
        puntaje = 10
        label_player = sg.Text('Jugador: {}'.format(nombre), background_color="Teal", font=('Helvetica', 20),
                               justification='center', key='text')
        label_PuntajeJ = sg.Text('puntaje: {}'.format(puntaje), background_color="Teal",
                                 font=('Helvetica', 20),
                                 justification='center', key='text')
        label_maquina = sg.Text('Maquina', background_color="Teal", font=('Helvetica', 20), justification='center',
                                key='text')
        label_PuntajeM = sg.Text('puntaje: {}'.format(puntaje), background_color="Teal",
                                 font=('Helvetica', 20),
                                 justification='center', key='text')
        # JUNTO FILAS Y COLUMNAS
        statecolor = ['lightgray', 'tan', 'yellow', 'lightblue', 'orange', 'limegreen', 'pink', 'red', 'darkgray']

        camTurno = sg.Button('Cambiar turno', button_color=('black', statecolor[4]), key='cambiar turno',
                             font=("Arial", 12, "bold"))
        camFichas = sg.Button('Cambiar fichas', button_color=('black', statecolor[4]), key='cambiar fichas',
                              font=("Arial", 12, "bold"), pad=(0, 80))
        col22 = [camTurno, camFichas]
        col2 = [[label_player], [label_PuntajeJ], player,col22]

        guaPartida = sg.Button('Guardar partida', button_color=('black', statecolor[4]), key='Guardar partida',
                               size=(8, 2), font=("Arial", 12, "bold"))
        termi = sg.Button('Terminar juego', button_color=('black', statecolor[4]), key='Terminar juego', size=(8, 2),
                          font=("Arial", 12, "bold"), pad=(50, 200))
        col00 = [guaPartida, termi]
        col01 = [self.r.dameLayout()[0][0], self.r.dameLayout()[1][0]]
        
        col0 = [[label_maquina], [label_PuntajeM], pc,col00]
        col1= [col01,[tablero]]


        layout = [[sg.Column(col0),sg.Column(col1) , sg.Column(col2)]]
        window = sg.Window('Ejercicio1', ).Layout(layout).Finalize()
        g = window.FindElement('_GRAPH_')
        
        for row in range(15):
            for col in range(15):
                #event, values = window.Read()
                matriz[row][col] = g.DrawRectangle((row * self.tam_celda + 5, col * self.tam_celda + 5), (row * self.tam_celda + self.tam_celda + 5, col * self.tam_celda + self.tam_celda + 5), line_color='black')
                tupla=(row,col)
                if (tupla in self.casillas_palabra_x2):
                    colorear_canvas(row,col, self.diccionario_colores["Azul"]) #Pinta Azul
                    g.DrawText("Px2", (row * self.tam_celda+11, col * self.tam_celda+9), color="White",font=("Arial",7, "bold"))
                    self.matriz_puntaje[row][col]="Px2"   
                elif (tupla in self.casillas_palabra_x3):
                    colorear_canvas(row,col,self.diccionario_colores["Rojo"]) #Pinta Rojo
                    g.DrawText("Px3", (row * self.tam_celda+11, col * self.tam_celda+9), color="White",font=("Arial",7, "bold"))
                    self.matriz_puntaje[row][col]="Px3"   
                elif (tupla in self.casillas_letra_x2):
                    colorear_canvas(row,col, self.diccionario_colores["Verde"]) #Pinta Verde
                    g.DrawText("Lx2", (row * self.tam_celda+11, col * self.tam_celda+9), color="White",font=("Arial",7, "bold"))
                    self.matriz_puntaje[row][col]="Lx2" 
                elif (tupla in self.casillas_letra_x3):
                    colorear_canvas(row,col, self.diccionario_colores["Amarillo"]) #Pinta Amarillo
                    g.DrawText("Lx3", (row * self.tam_celda+11, col * self.tam_celda+9), color="White",font=("Arial",7, "bold"))
                    self.matriz_puntaje[row][col]="Lx3" 
                elif (tupla in self.casillas_letra_resto1):
                    colorear_canvas(row,col, self.diccionario_colores["Rosado"]) #Pinta Rosado
                    g.DrawText("P-1", (row * self.tam_celda+11, col * self.tam_celda+9), color="White",font=("Arial",7, "bold"))
                    self.matriz_puntaje[row][col]="P-1"
                elif (tupla in self.casillas_letra_resto2):
                    colorear_canvas(row,col,self.diccionario_colores["Naranja"]) #Pinta Naranja
                    g.DrawText("P-2", (row * self.tam_celda+11, col * self.tam_celda+9), color="White", font=("Arial",7, "bold"), )
                    self.matriz_puntaje[row][col]="P-2"
                elif (tupla in self.casillas_letra_resto3):
                    colorear_canvas(row,col, self.diccionario_colores["Marron"]) #Pinta Marron
                    g.DrawText("P-3", (row * self.tam_celda+11, col * self.tam_celda+9), color="White", font=("Arial",7, "bold"))
                    self.matriz_puntaje[row][col]="P-3"
        self.tablero=window
#------------------------Funciones de interaccion con el tablero--------------------------------
    def dibujarLetra(self, coord_x, coord_y, letra):
        g=self.tablero.FindElement('_GRAPH_')
        self.text_box[coord_x][coord_y] = letra
        g.DrawText(letra, (coord_x * self.tam_celda + 17, coord_y * self.tam_celda + 18), font=("Arial", 12, "bold"))
        #event=self.tablero.Read() #servian para ver el dibujo del tablero

    def marcarLetra(self, letra):
        self.tablero.FindElement(letra).Update(button_color=('white', 'blue'))
        #event=self.tablero.Read() #servian para ver q ver el dibujo del tablero
        
    def desmarcarLetra(self, letra):
        self.tablero.FindElement(letra).Update(button_color=('white', 'green'))
        #event=self.tablero.Read() #servian para ver q ver el dibujo del tablero 
#-------------------Funciones de funcionalidad------------------------------------------
    def esConsecutivaEnX(self, coordX, coordY, pos1erLetraX):
        ok=False
        if (coordX>self.pos1erLetraX and self.selected[coordX-1][coordY]==True):
            #el anterior a mi izquierda tiene q estar ocupado
            ok=True
        elif (coordX<self.pos1erLetraX and self.selected[coordX+1][coordY]==True):
            #el posterior a mi izquierda tiene q estar ocupado
            ok=True
        return ok
    def esConsecutivaEnY(self, coordX, coordY, pos1erLetraY):
        ok=False
        if (coordY>self.pos1erLetraY and self.selected[coordX][coordY-1]==True):
            #el de arriba mio tiene q estar ocupado
            ok=True
        elif (coordY<self.pos1erLetraY and self.selected[coordX][coordY+1]==True):
            #el de abajo mio tiene q estar ocupado
            ok=True
        return ok

    def validarPosicion(self,letraActual,coordX,coordY):
        ok=False
        if (coordX < 15 or coordY < 15):
        #Primero: Tiene que estar adentro del tablero
            if (self.selected[coordX][coordY]==False):
            #Segundo: La casilla que seleccione efectivamente no tiene que tener letras (esta libre).
                if (letraActual=="1erLetra"):
                    self.pos1erLetraX=coordX
                    self.pos1erLetraY=coordY
                    ok=True
                elif (letraActual=="2daLetra"):
                    if (coordX>self.pos1erLetraX and coordY==self.pos1erLetraY and self.esConsecutivaEnX(coordX,coordY,self.pos1erLetraX)):
                        self.sentido="HORIZONTAL"
                        ok=True
                    elif (coordX<self.pos1erLetraX and coordY==self.pos1erLetraY and self.esConsecutivaEnX(coordX,coordY,self.pos1erLetraX)):
                        self.sentido="HORIZONTAL"
                        ok=True
                    elif (coordY>self.pos1erLetraY and coordX==self.pos1erLetraX and self.esConsecutivaEnY(coordX,coordY, self.pos1erLetraY)):
                        self.sentido="VERTICAL"
                        ok=True
                    elif (coordY<self.pos1erLetraY and coordX==self.pos1erLetraX and self.esConsecutivaEnY(coordX,coordY, self.pos1erLetraY)):
                        self.sentido="VERTICAL"
                        ok=True
                elif (letraActual=="LetrasRestantes"):
                    if (self.sentido=="HORIZONTAL"):
                        if (coordX>self.pos1erLetraX and coordY==self.pos1erLetraY and self.esConsecutivaEnX(coordX,coordY,self.pos1erLetraX)):
                            ok=True
                        elif (coordX<self.pos1erLetraX and coordY==self.pos1erLetraY and self.esConsecutivaEnX(coordX,coordY,self.pos1erLetraX)):
                            ok=True
                    elif (self.sentido=="VERTICAL"):
                        if (coordY>self.pos1erLetraY and coordX==self.pos1erLetraX and self.esConsecutivaEnY(coordX,coordY, self.pos1erLetraY)):
                            ok=True
                        elif (coordY<self.pos1erLetraY and coordX==self.pos1erLetraX and self.esConsecutivaEnY(coordX,coordY, self.pos1erLetraY)):
                            ok=True    
        return ok
    def colocarLetra(self, coordX, coordY):
        if (self.validarPosicion(self.letraActual, coordX, coordY)):
            self.selected[coordX][coordY] = True    #Marca ocupada la casilla
            tupla=(coordX,coordY)
            self.listaPos.append(tupla)             #Guardo la posicion en una lista.      
            if (self.letraActual=="1erLetra"):
                self.letraActual="2daLetra"
            elif (self.letraActual=="2daLetra"):
                self.letraActual="LetrasRestantes"
            self.dibujarLetra(coordX, coordY, self.boton_actual)
            self.liberarLetra(self.boton_actual)
            
    def seleccionarLetra(self, letra):
        if (self.boton_seleccionado==False and self.boton_actual!=letra):
            self.boton_seleccionado=True
            self.marcarLetra(letra)
            self.boton_actual=letra
        elif (self.boton_seleccionado==True and self.boton_actual==letra):
            self.boton_seleccionado=False
            self.desmarcarLetra(letra)
            self.boton_actual=None
    def liberarLetra(self, letra):
        self.boton_seleccionado=False
        self.desmarcarLetra(letra)
        self.tablero.FindElement(letra).Update(" ")   
        self.boton_actual=None
         
    def funcion(self, event, values):
        if 'tipo' == 'Exit' or event is None:
            self.cortaTodo=True 
        elif event=='__TIMEOUT__':
            # acualizar tiempo
            FinJuego = self.r.finJuego()
            if (FinJuego == True):
                # if(r.una==0):
                #   print("Hola")
                #print("hola")
                if (self.r.una == 1):
                    self.tablero['reloj'].update(
                        'Tiempo: {:02d}:{:02d}.{:02d}'.format((self.r.counter // 100) // 60, (self.r.counter // 100) % 60,
                                                      self.r.counter % 100))
                    #print("chau")
            if (FinJuego == False):
                # print("entre al else")
                self.r.una = 0;
                self.tablero['reloj'].update(
                    'Tiempo: 01:00:00')

            self.r.counter += 1
            #self.r.TurnoDeComputadora()
            j = FinJuego;   
        else: 
            if (event != "_GRAPH_"):
                #significa q presione algun boton. 
                #Ver como solucionar presionar botones q no deberia. 
                self.seleccionarLetra(event)
            else:
                if (self.boton_actual != None):
                    mouse = values["_GRAPH_"]
                    coordX=mouse[0] // self.tam_celda
                    coordY=mouse[1] // self.tam_celda
                    self.colocarLetra(coordX, coordY)

    def correrTablero(self):  
        lista_letras=["A","E","I","O","U"]
        self.dibujarTablero(self.matriz,lista_letras)
        while (True):
            if (self.cortaTodo):
                break
            event, values=self.tablero.read(timeout=10)
            self.funcion(event,values)
            print(self.listaPos)
#Pruebas de tablero
if __name__ == "__main__":
    tablero = Tablero()
    lista_letras=["A","E","I","O","U"]
    tablero.dibujarTablero(tablero.matriz,lista_letras)
    while (True):
        if (tablero.cortaTodo):
            break
        event, values=tablero.tablero.read(timeout=10)
        tablero.funcion(event,values)
        print(tablero.listaPos)