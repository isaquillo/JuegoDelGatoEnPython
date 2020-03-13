# Programa que simula el Juego del Gato en Modo Consola
# Autor: Isaac Larios Díaz
# Fecha: 18 de Julio 2016
# Última modificación:

# Variables globales
nFilas = 3
nColumnas = 3
maxTurnos = 9
tablero = [["", "", ""], ["", "", ""], ["", "", ""]]
hayGanador = False
simboloGanador = "X"
simboloActual = "X"
turnosJugados = 0
turnosAgotados = False

# Declaración de funciones
def pausar(mensaje):
    input("Pulsa una tecla para " + mensaje)

def limpia_pantalla():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def inicializa_tablero():
    global tablero
    for fila in range(nFilas):
        for columna in range(nColumnas):
            tablero[fila][columna] = " "


def imprime_tablero():
    global tablero
    limpia_pantalla()
    for i in range(nFilas):
        print("[" + tablero[i][0] + "] " + "[" + tablero[i][1] + "] " +
              "[" + tablero[i][2] + "]")


def juega_turno():
    global tablero
    global simboloActual
    global turnosJugados
    fila = 0
    columna = 0
    es_posicion_valida = False
    es_posicion_disponible = False
    while not es_posicion_disponible:
        while not es_posicion_valida:
            imprime_tablero()
            print("Es turno del jugador " + simboloActual)
            fila = int(input("Dime la fila (1-3): ",))
            columna = int(input("Dime la columna (1-3): "))
            if (fila >= 1 and fila <= 3) and (columna >= 1 and columna <= 3):
                es_posicion_valida = True
            else:
                print("Posición inválida. Vuelve a elegir")
                pausar("continuar")

        if tablero[fila - 1][columna - 1] == " ":
            es_posicion_disponible = True
            tablero[fila - 1][columna - 1] = simboloActual
            turnosJugados += 1
            if simboloActual == "X":
                simboloActual = "O"
            else:
                simboloActual = "X"
        else:
            print("Ese espacio no está disponible. Vuelve a elegir")
            pausar("continuar")
            es_posicion_valida = False

def verifica_estado_tablero():
    global tablero
    global turnosJugados
    global hayGanador
    global simboloGanador
    global turnosAgotados
    imprime_tablero()
    if turnosJugados == maxTurnos:
        turnosAgotados = True

    # Verifica filas y columnas
    for i in range(nFilas):
        if tablero[i][0] != " " and tablero[i][0] == tablero[i][1] and tablero[i][1] == tablero[i][2]:
            hayGanador = True
            simboloGanador = tablero[i][0]
        elif tablero[0][i] != " " and tablero[0][i] == tablero[1][i] and tablero[1][i] == tablero[2][i]:
            hayGanador = True
            simboloGanador = tablero[0][i]

    # Verifica diagonales
    if tablero[0][0] != " " and tablero[0][0] == tablero[1][1] and tablero[1][1] == tablero[2][2]:
        hayGanador = True
        simboloGanador = tablero[0][0]
    elif tablero[2][0] != " " and tablero[2][0] == tablero[1][1] and tablero[1][1] == tablero[0][2]:
        hayGanador = True
        simboloGanador = tablero[2][0]


def imprime_resultados():
    global turnosAgotados
    global hayGanador
    if turnosAgotados and not hayGanador:
        print("Empate")
    else:
        print("Gana el jugador " + simboloGanador)


def desea_continuar_juego():
    respuesta = " "
    es_respuesta_valida = False
    continua_juego = True
    while not es_respuesta_valida:
        respuesta = str(input("Quieres jugar otra partida: "))
        respuesta.lower()
        if respuesta == "s":
            es_respuesta_valida = True
        elif respuesta == "n":
            es_respuesta_valida = True
            continua_juego = False
        else:
            print("Opcion no válida. Vuelve a elegir")
            pausar("continuar")
    return continua_juego

# Ejecución del programa

continuaJuego = True
while continuaJuego:
    inicializa_tablero()
    turnosAgotados = False
    hayGanador = False

    while not hayGanador and not turnosAgotados:
        juega_turno()
        verifica_estado_tablero()

    imprime_resultados()
    continuaJuego = desea_continuar_juego()

pausar("terminar")
