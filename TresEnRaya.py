"""
 _____                                       
|____ |                                      
    / /   ___ _ __    _ __ __ _ _   _  __ _  
    \ \  / _ \ '_ \  | '__/ _` | | | |/ _` | 
.___/ / |  __/ | | | | | | (_| | |_| | (_| | 
\____/   \___|_| |_| |_|  \__,_|\__, |\__,_| 
                                 __/ |       
                                |___/        © Rasphy 2023
"""

import tkinter 

def crearTablero(filas, columnas): # Crea el tablero con listas
    global tablero
    tablero = []
    for x in range(filas):
        tablero.append([])
        for y in range(columnas):
            tablero[x].append(" ")

def mostrarTablero(): # Muestra el tablero en consola
    # Numeros de columnas
    print("_|", end="")
    for z in range(len(tablero[0])):
        print(z+1, end="|")
    print("")

    # Fichas
    numerosLaterales = filasTablero
    for x in tablero:
        numerosLaterales = numerosLaterales - 1
        print("{}|".format(filasTablero - numerosLaterales), end="")
        for y in x:
            print(y, end="")
            print("|", end="")
        print("")

    # Linea inferior
    print("-+", end="")
    for x in range(len(tablero[0])):
        print("-",end="+")
    print("")

def turnos(fila, columna, boton):
    columnaElegida = fila
    filaElegida = columna
    if boton["text"] == "":
        global jugadorActual
        if jugadorActual == 1:
            tablero[columnaElegida][filaElegida] = "X"
            boton.config(text= "X", font=("helvetica", 9))
            indicadorJugadorActual.config(text="Turno del jugador 2")
            comprobarVictoria()
            jugadorActual = 2
            mostrarTablero()
        else: 
            tablero[columnaElegida][filaElegida] = "O"
            boton.config(text= "O")
            indicadorJugadorActual.config(text="Turno del jugador 1")
            comprobarVictoria()
            jugadorActual = 1
            mostrarTablero()

    else:
        return

def comprobarVictoria():
    # Comprobar filas
    for columna in range(columnasTablero+1):
        coincidencias = 0
        for fila in range(filasTablero+1):
            if jugadorActual == 1:
                if tablero[filasTablero-columna][fila] != "X":
                    coincidencias = 0
                else:
                    coincidencias = coincidencias + 1
                    if coincidencias >= 3:
                        mostrarTablero()
                        indicadorJugadorActual.config(text="Gana el jugador 1")
                        desactivarBotones()
            if jugadorActual == 2:
                if tablero[filasTablero-columna][fila] != "O":
                    coincidencias = 0
                else:
                    coincidencias = coincidencias + 1
                    if coincidencias >= 3:
                        mostrarTablero()
                        indicadorJugadorActual.config(text="Gana el jugador 2")
                        desactivarBotones()
    # Comprobar columnas
    for fila in range(filasTablero+1):
        coincidencias = 0
        for columna in range(columnasTablero+1):
            if jugadorActual == 1:
                if tablero[filasTablero-columna][fila] != "X":
                    coincidencias = 0
                else:
                    coincidencias = coincidencias + 1
                    if coincidencias >= 3:
                        mostrarTablero()
                        indicadorJugadorActual.config(text="Gana el jugador 1")
                        desactivarBotones()
            if jugadorActual == 2:
                if tablero[filasTablero-columna][fila] != "O":
                    coincidencias = 0
                else:
                    coincidencias = coincidencias + 1
                    if coincidencias >= 3:
                        mostrarTablero()
                        indicadorJugadorActual.config(text="Gana el jugador 2")
                        desactivarBotones()
    # Comprobar Diagonales Izq-Dch
    for x in range(filasTablero+1):
        coincidencias = 0
        for fila in range(filasTablero+1):
            if jugadorActual == 1:
                if tablero[filasTablero-fila-x][fila] != "X":
                    coincidencias = 0
                else:
                    coincidencias = coincidencias + 1
                    if coincidencias >= 3:
                        mostrarTablero()
                        indicadorJugadorActual.config(text="Gana el jugador 1")
                        desactivarBotones()
            if jugadorActual == 2:
                if tablero[filasTablero-fila-x][fila] != "O":
                    coincidencias = 0
                else:
                    coincidencias = coincidencias + 1
                    if coincidencias >= 3:
                        mostrarTablero()
                        indicadorJugadorActual.config(text="Gana el jugador 2")
                        desactivarBotones()

    # Comprobar Diagonales Dch-Izq
    for x in range(filasTablero+1):
        coincidencias = 0
        for fila in range(filasTablero+1):
            if jugadorActual == 1:
                if tablero[-(fila+1)][filasTablero-fila-x] != "X":
                    coincidencias = 0
                else:
                    coincidencias = coincidencias + 1
                    if coincidencias >= 3:
                        mostrarTablero()
                        print("Gana el jugador 1")
                        indicadorJugadorActual.config(text="Gana el jugador 1")
                        desactivarBotones()
            if jugadorActual == 2:
                if tablero[-(fila+1)][filasTablero-fila-x] != "O":
                    coincidencias = 0
                else:
                    coincidencias = coincidencias + 1
                    if coincidencias >= 3:
                        mostrarTablero()
                        print("Gana el jugador 2")
                        indicadorJugadorActual.config(text="Gana el jugador 2")
                        desactivarBotones()

def empezarJuego():
    global filasTablero
    global columnasTablero

    filasTablero = 3-1
    columnasTablero = 3-1

    crearTablero(3, 3) # Crea un tablero (x = filas, y = columnas)
    mostrarTablero() # Mostrar tablero

def desactivarBotones():
    boton1.config(state="disabled")
    boton2.config(state="disabled")
    boton3.config(state="disabled")
    boton4.config(state="disabled")
    boton5.config(state="disabled")
    boton6.config(state="disabled")
    boton7.config(state="disabled")
    boton8.config(state="disabled")
    boton9.config(state="disabled")

# Variables
global jugadorActual
jugadorActual = 1

ventana = tkinter.Tk()
ventana.geometry("300x330")
ventana.title("Tres en raya")
ventana.iconbitmap("C:/Users/rasph/Desktop/Programar/Python/TresEnRaya/v2.0/icon.ico")

frame1 = tkinter.Frame(ventana)
frame1.pack()

frame2 = tkinter.Frame(ventana)
frame2.pack()

#------TiTulo------
titulo = tkinter.Label(frame1, text="Tres en raya", font=("calibri bold", 20))
titulo.pack()

#------Botones------
# Fila 1
boton1 = tkinter.Button(frame2, command=lambda: turnos(0, 0, boton1), text="", width=10, height=5)
boton1.grid(row=0, column= 1)

boton2 = tkinter.Button(frame2, command=lambda: turnos(0, 1, boton2), text="", width=10, height=5)
boton2.grid(row=0, column= 2)

boton3 = tkinter.Button(frame2, command=lambda: turnos(0, 2, boton3), text="", width=10, height=5)
boton3.grid(row=0, column= 3)

# Fila 2
boton4 = tkinter.Button(frame2, command=lambda: turnos(1, 0, boton4), text="", width=10, height=5)
boton4.grid(row=1, column= 1)

boton5 = tkinter.Button(frame2, command=lambda: turnos(1, 1, boton5), text="", width=10, height=5)
boton5.grid(row=1, column= 2)

boton6 = tkinter.Button(frame2, command=lambda: turnos(1, 2, boton6), text="", width=10, height=5)
boton6.grid(row=1, column= 3)

# Fila 3
boton7 = tkinter.Button(frame2, command=lambda: turnos(2, 0, boton7), text="", width=10, height=5)
boton7.grid(row=2, column= 1)

boton8 = tkinter.Button(frame2, command=lambda: turnos(2, 1, boton8), text="", width=10, height=5)
boton8.grid(row=2, column= 2)

boton9 = tkinter.Button(frame2, command=lambda: turnos(2, 2, boton9), text="", width=10, height=5)
boton9.grid(row=2, column= 3)

#------Jugador Actual------
indicadorJugadorActual = tkinter.Label(frame1, text= "Turno del jugador {}".format(jugadorActual))
indicadorJugadorActual.pack()

empezarJuego()

ventana.mainloop()