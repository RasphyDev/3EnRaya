"""
 _____                                       
|____ |                                      
    / /   ___ _ __    _ __ __ _ _   _  __ _  
    \ \  / _ \ '_ \  | '__/ _` | | | |/ _` | 
.___/ / |  __/ | | | | | | (_| | |_| | (_| | 
\____/   \___|_| |_| |_|  \__,_|\__, |\__,_| 
                                 __/ |       
                                |___/        
"""
# Variables
global jugadorActual
jugadorActual = 1

def crearTablero(filas, columnas): # Crea el tablero con listas
    global tablero
    tablero = []
    for x in range(filas):
        tablero.append([])
        for y in range(columnas):
            tablero[x].append(" ")

def mostrarTablero(): # Muestra el tablero en consola
    # Numeros de columnas
    print("|", end="")
    for z in range(len(tablero[0])):
        print(z+1, end="|")
    print("")

    # Fichas
    for x in tablero:
        print("|", end="")
        for y in x:
            print(y, end="")
            print("|", end="")
        print("")

    # Linea inferior
    print("+", end="")
    for x in range(len(tablero[0])):
        print("-",end="+")
    print("")

def turnos(jugadorActual):
    # Muestra el jugador actual
    if jugadorActual == 1:
        print("Turno del jugador 1")
    elif jugadorActual == 2:
        print("Turno del jugador 2")

    # Pregunta al jugador el numero de una columna
    columnaElegida = input("Escribe el numero de una columna: ")
    try:
        int(columnaElegida)
    except:
        mostrarTablero()
        print("Escribe una columna valida")
        turnos(jugadorActual)

    if int(columnaElegida) <= len(tablero[0]):
        ponerFicha(int(columnaElegida))

    else:
        mostrarTablero()
        print("Escribe una columna valida")
        turnos(jugadorActual)

def ponerFicha(columnaElegida):
    for columna in range(-(len(tablero)), 0):
        if " " in tablero[(columna*-1)-1][columnaElegida-1]:
            global jugadorActual
            if jugadorActual == 1:
                tablero[(columna*-1)-1][columnaElegida-1] = "X"
                comprobarVictoria((columna*-1)-1, columnaElegida-1)
                jugadorActual = 2
            else: 
                tablero[(columna*-1)-1][columnaElegida-1] = "O"
                comprobarVictoria((columna*-1)-1, columnaElegida-1)
                jugadorActual = 1
            mostrarTablero()
            turnos(jugadorActual)

        elif columna >= -1 :
            mostrarTablero()
            print("Escribe en una columna vacia")
            turnos(jugadorActual)

def comprobarVictoria(columnaActual, filaActual):
    # Comprobar filas
    for columna in range(columnasTablero):
        coincidencias = 0
        for fila in range(filasTablero):
            if jugadorActual == 1:
                if tablero[filasTablero-columna][fila] != "X":
                    coincidencias = 0
                else:
                    coincidencias = coincidencias + 1
                    if coincidencias >= 3:
                        mostrarTablero()
                        print("Gana el jugador 1")
                        exit()
            if jugadorActual == 2:
                if tablero[filasTablero-columna][fila] != "O":
                    coincidencias = 0
                else:
                    coincidencias = coincidencias + 1
                    if coincidencias >= 3:
                        mostrarTablero()
                        print("Gana el jugador 2")
                        exit()
    # Comprobar columnas
    for fila in range(filasTablero):
        coincidencias = 0
        for columna in range(columnasTablero):
            if jugadorActual == 1:
                if tablero[filasTablero-columna][fila] != "X":
                    coincidencias = 0
                else:
                    coincidencias = coincidencias + 1
                    if coincidencias >= 3:
                        mostrarTablero()
                        print("Gana el jugador 1")
                        exit()
            if jugadorActual == 2:
                if tablero[filasTablero-columna][fila] != "O":
                    coincidencias = 0
                else:
                    coincidencias = coincidencias + 1
                    if coincidencias >= 3:
                        mostrarTablero()
                        print("Gana el jugador 2")
                        exit()
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
                        print("Gana el jugador 1")
                        exit()
            if jugadorActual == 2:
                if tablero[filasTablero-fila-x][fila] != "O":
                    coincidencias = 0
                else:
                    coincidencias = coincidencias + 1
                    if coincidencias >= 3:
                        mostrarTablero()
                        print("Gana el jugador 2")
                        exit()

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
                        exit()
            if jugadorActual == 2:
                if tablero[-(fila+1)][filasTablero-fila-x] != "O":
                    coincidencias = 0
                else:
                    coincidencias = coincidencias + 1
                    if coincidencias >= 3:
                        mostrarTablero()
                        print("Gana el jugador 2")
                        exit()

crearTablero(6, 6) # Crea un tablero (x = filas, y = columnas)
filasTablero = 6-1
columnasTablero = 6-1
mostrarTablero() # Mostrar tablero

turnos(jugadorActual)