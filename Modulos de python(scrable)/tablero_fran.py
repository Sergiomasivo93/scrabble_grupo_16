import PySimpleGUI as sg
class Tablero:
    tam_celda=0
    matriz = []
    selected = []
    text_box = []
    matriz_puntaje=[]
    casillas_palabra_x3=[]
    casillas_palabra_x2=[]
    casillas_letra_x3=[]
    casillas_letra_x2=[]
    casillas_letra_resto1=[]
    casillas_letra_resto2=[]
    casillas_letra_resto3=[]
    tablero = None
    diccionario_colores={"Rojo":"#ea3232","Azul":"#4b7eea","Verde":"#50ea4b","Amarillo":"#c4bc00","Rosado":"#fd73f0","Naranja":"#fb981e","Marron":"#b46708"}
    def botonConfig(self, texto):
        #funciona
        color_button = ('white', 'green') #primer parametro:color de letra, segundo parametro: color fondo
        tam_button = 10, 5
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
        tamaño=(650,650) #tamaño total del canvas
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
        
        colorear_canvas= lambda x, y, z: g.TKCanvas.itemconfig(self.matriz[x][y], fill=z) #Azul - Palabrax2
        """
        puntaje_palabra_x3 = lambda x, y, z: g.TKCanvas.itemconfig(self.matriz[x][y], fill="#ea3232") #Rojo- Palabrax3
        puntaje_letra_x2 =lambda x, y, z: g.TKCanvas.itemconfig(self.matriz[x][y], fill="#50ea4b") #Verde - Letrax2
        puntaje_letra_x3 =lambda x, y, z: g.TKCanvas.itemconfig(self.matriz[x][y], fill="#fdf658") #Amarillo - Letrax3
        puntaje_palabra_resto1 =lambda x, y, z: g.TKCanvas.itemconfig(self.matriz[x][y], fill="#fd73f0") #Rosado - Resto1
        puntaje_palabra_resto2 =lambda x, y, z: g.TKCanvas.itemconfig(self.matriz[x][y], fill=z) #Naranja - Resto2
        puntaje_palabra_resto3 =lambda x, y, z: g.TKCanvas.itemconfig(self.matriz[x][y], fill="#b46708") #Marron - Resto3
        """
        boton=lambda texto:self.botonConfig(texto)
        tablero=self.tableroConfig()
        self.coordenadasColor()
        layout=[[tablero],                 
                [boton(texto) for texto in lista_letras]
                ]
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
    #tratar de achicar la letra de la ezquina superior izquierda
    #tratar de acerla gris
    #opcion con ayuda sin ayuda

    def dibujarLetra(self, coord_x, coord_y, letra):
        g=self.tablero.FindElement('_GRAPH_')
        box_x = coord_x #// self.tam_celda
        box_y = coord_y #// self.tam_celda
        if box_x < 15 or box_y < 15:
            if (self.selected[box_x][box_y] == False):   
                self.selected[box_x][box_y] = True
                self.text_box[box_x][box_y] = letra
                g.DrawText(letra, (box_x * self.tam_celda + 17, box_y * self.tam_celda + 18), font=("Arial", 12, "bold"))
            else:
                print ("Ya se escribio en esa casilla")
        event=self.tablero.Read()

    def marcarLetra(self, letra):
        self.tablero.FindElement(letra).Update(button_color=('white', 'blue'))
        event=self.tablero.Read()
        
    def desmarcarLetra(self, letra):
        self.tablero.FindElement(letra).Update(button_color=('white', 'green'))
        event=self.tablero.Read()
        
        
        
"""
tablero = Tablero()
lista_letras=["A","E","I","O","U"]
tablero.dibujarTablero(tablero.matriz,lista_letras)
tablero.dibujarLetra(0,0, "O")
tablero.dibujarLetra(0,0, "A")
tablero.marcarLetra("A")
tablero.desmarcarLetra("A")
"""
