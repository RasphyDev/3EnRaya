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
pantallaInicio= """
_|1|2|3|
3| | | |
e|n| | |
r|a|y|a|
-+-+-+-+"""
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

def turnos(jugadorActual):
    # Muestra el jugador actual
    if jugadorActual == 1:
        print("Turno del jugador 1")
    elif jugadorActual == 2:
        print("Turno del jugador 2")

    # Pregunta al jugador el numero de una columna
    columnaElegida = input("Escribe el numero de una columna: ")
    filaElegida = input("Escribe el numero de una fila: ")
    try:
        int(columnaElegida)
        int(filaElegida)
    except:
        mostrarTablero()
        print("Escribe una columna/fila valida")
        turnos(jugadorActual)

    if int(columnaElegida) <= len(tablero[0]) and int(filaElegida) <= len(tablero[0]):
        ponerFicha(int(columnaElegida), int(filaElegida))

    else:
        mostrarTablero()
        print("Escribe una columna/fila valida")
        turnos(jugadorActual)

def ponerFicha(columnaElegida, filaElegida):
    if " " in tablero[filaElegida-1][columnaElegida-1]:
        global jugadorActual
        if jugadorActual == 1:
            tablero[filaElegida-1][columnaElegida-1] = "X"
            comprobarVictoria()
            jugadorActual = 2
            mostrarTablero()
        else: 
            tablero[filaElegida-1][columnaElegida-1] = "O"
            comprobarVictoria()
            jugadorActual = 1
            mostrarTablero()
        turnos(jugadorActual)

    else:
        mostrarTablero()
        print("Escribe en un espacio vacio.")
        turnos(jugadorActual)

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

def empezarJuego():
    global filasTablero
    global columnasTablero
    filasTablero = input("Escribe el numero de filas y columnas del tablero: ")
    try:
        int(filasTablero)
    except:
        print("Escribe un numero valido")
        empezarJuego()
        return

    filasTablero = int(filasTablero)-1
    columnasTablero = filasTablero

    if filasTablero+1 and columnasTablero+1 < 3:
        print("¡El tablero no puede ser tan pequeño!")
        empezarJuego()

    else:
        if filasTablero+1 and columnasTablero+1 > 9:
            print("¡El tablero no puede ser tan grande!")
            empezarJuego()

    crearTablero(filasTablero+1, columnasTablero+1) # Crea un tablero (x = filas, y = columnas)
    mostrarTablero() # Mostrar tablero

print(pantallaInicio)
empezarJuego()
turnos(jugadorActual)