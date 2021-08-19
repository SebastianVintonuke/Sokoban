import soko
import gamelib
import backtracking

coordenadas = {'NORTE':(0, -1),'OESTE':(-1, 0),'SUR':(0, 1),'ESTE':(1, 0)}
tamaño_imagen = 64 #pixeles

def importa_niveles(nombre_archivo):
    """Recibe un archivo con la descripcion de los niveles de la forma:
    Level n                    # n DEBE SER ENTERO Y ÚNICO.
    "Título del nivel"         # PRECINDIBLE. EN CASO DE TENER, EL TITULO NO DEBE EMPEZAR CON LOS SIGUIENTES CARACTERES: # @$.*+
    Descripción fila 1
    Descripción fila 2         # CONSULTE MODULO SOKO.PY PARA VER UNA DESCRIPCIÓN DEL ESTADO INICIAL DE LAS FILAS.
    ...
    Descripcion fila n
                               # LÍNEA VACÍA.
    Level n+1
    ...

    """
    niveles={}
    nivel=[]
    with open(nombre_archivo) as archivo:
        for linea in archivo:
            if linea != "\n":
                nivel.append(linea.rstrip("\n"))
            else:
                if nivel[1][0] in "# @$.*+":
                    niveles[nivel[0]] = ["Sin Título",nivel[1:]]
                else:
                    niveles[nivel[0]] = [nivel[1],nivel[2:]]
                nivel = []
        if nivel [1][0] in "# @$.*+":
            niveles[nivel[0]] = ["Sin Título",nivel[1:]]
        else:
            niveles[nivel[0]] = [nivel[1],nivel[2:]]
    return niveles

def agrega_espacios(diccionario_de_niveles):
    """Agrega espacios al final de las filas que tienen menos columnas que el resto, de tal forma que todas las filas tengan el mismo número de columnas"""
    for clave in diccionario_de_niveles:
        columnas = 0
        grilla = diccionario_de_niveles[clave][1]
        for fila in range(0,len(grilla)):
            if len(grilla[fila])>columnas:
                columnas=len(grilla[fila])
        for fila in range(0,len(grilla)):
            if len(grilla[fila])<columnas:
                espacios = columnas-len(grilla[fila])
                fila_arreglada = grilla[fila] + espacios * " "
                diccionario_de_niveles[clave][1][fila]=fila_arreglada
    return diccionario_de_niveles

def juego_mostrar(grilla,tamaño_imagen):
    """Actualizar la ventana"""
    dimension = soko.dimensiones(grilla)
    for f in range (0,dimension[1]):
        for c in range (0,dimension[0]):
            x = tamaño_imagen * c
            y = tamaño_imagen * f
            gamelib.draw_image('img/ground.gif', x, y)
            if soko.hay_objetivo(grilla, c, f):
                gamelib.draw_image('img/goal.gif', x, y)
            if soko.hay_jugador(grilla, c, f):
                gamelib.draw_image('img/player.gif', x, y)
            elif soko.hay_caja(grilla, c, f):
                gamelib.draw_image('img/box.gif', x, y)
            elif soko.hay_pared(grilla, c, f):
                gamelib.draw_image('img/wall.gif', x, y)

def importa_teclas(nombre_archivo):
    """Recibe un archivo de la forma:
    tecla1 = accion1            # CONSIDERAR QUE LAS TECLAS SON ÚNICAS. VARIAS TECLAS PUEDEN REALIZAR LA MISMA ACCIÓN, PERO NO SE PUEDEN REALIZAR VARIAS ACCIONES CON UNA MISMA TECLA.
    tecla2 = accion2            
    ...                         # PUEDE INCLUIR LINEAS VACÍAS.
    tecla3 = accion3
    """
    diccionario_teclas={}
    with open(nombre_archivo) as archivo:
        for linea in archivo:
            if linea != "\n":
                tecla, accion = (linea.rstrip("\n")).split(" = ")
                diccionario_teclas[tecla] = accion
    return diccionario_teclas

def inicializa_nivel(nivel,niveles,tamaño_imagen):
    gamelib.title("Level " + str(nivel) + " - " + niveles["Level "+str(nivel)][0])     
    grilla = soko.crear_grilla(niveles["Level "+str(nivel)][1])
    columnas, filas = soko.dimensiones(grilla)
    pixels_ancho = columnas * tamaño_imagen
    pixels_alto = filas * tamaño_imagen
    gamelib.resize(pixels_ancho, pixels_alto)
    return grilla

def inicializa_juego(movimientos):
    """Importa los datos del juego e inicializa el nivel inicial"""
    niveles = agrega_espacios(importa_niveles("niveles.txt"))
    teclas = importa_teclas("teclas.txt")
    nivel = 1 #Nivel inicial
    grilla = inicializa_nivel(nivel, niveles, tamaño_imagen)
    movimientos = soko.historial(grilla, movimientos)
    return niveles, teclas, nivel, grilla, movimientos

def inicializa_secuencias():
    """Inicializa las secuencias requeridas"""
    movimientos = []
    guia = []
    return movimientos, guia

def pista(grilla, movimientos, guia):
    """Si hay pistas disponibles se desencola una pista y se efectúa esa acción, si no; utilizando el algoritmo de backtracking para intentar encontrar la solución"""
    movimientos = soko.historial(grilla, movimientos)
    if not guia:
        guia = (backtracking.buscar_solucion(grilla)[1])
    else:
        grilla = soko.mover(grilla, guia.pop())
    return grilla, movimientos, guia

def reiniciar(grilla, movimientos, niveles, nivel):
    """Reinicia la grilla actual y la lista de movimientos"""
    movimientos = []
    grilla = soko.crear_grilla(niveles["Level "+str(nivel)][1])
    movimientos = soko.historial(grilla, movimientos)
    return grilla, movimientos

def pasar_nivel(grilla, movimientos, niveles, nivel):
    """Inicializa el siguiente nivel"""
    nivel += 1
    movimientos = []
    grilla = inicializa_nivel(nivel,niveles,tamaño_imagen)
    movimientos = soko.historial(grilla, movimientos)
    return grilla, movimientos, nivel

def realizar_movimiento(grilla, movimientos, tecla, guia):
    """Reinicia la guía de pistas, apila el último movimiento al historial y mueve al jugador"""
    guia = None
    movimientos = soko.historial(grilla, movimientos)
    grilla = soko.mover(grilla, coordenadas[tecla])
    return grilla, movimientos, guia


def main():
    # Inicializar el estado del juego
    movimientos, guia = inicializa_secuencias()
    niveles, teclas, nivel, grilla, movimientos = inicializa_juego(movimientos)

    while gamelib.is_alive():
        gamelib.draw_begin()
        juego_mostrar(grilla,tamaño_imagen) # Dibujar la pantalla
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        
        if not ev:
            break

        if soko.juego_ganado(grilla):
            gamelib.play_sound('sound/Menu2A.wav')
            grilla, movimientos, nivel = pasar_nivel(grilla, movimientos, niveles, nivel)

        tecla = teclas.get(ev.key, None)
        # Actualizar el estado del juego, según la 'tecla' presionada

        if tecla == 'SALIR':
            break
        
        if tecla == 'REINICIAR':
            gamelib.play_sound('sound/Menu2A.wav')
            grilla, movimientos = reiniciar(grilla, movimientos, niveles, nivel)

        if tecla == 'DESHACER':
            gamelib.play_sound('sound/stepstone_1.wav')
            grilla = soko.deshacer(movimientos)

        if tecla == "PISTA":
            gamelib.play_sound('sound/stepstone_1.wav')
            grilla, movimientos, guia = pista(grilla, movimientos, guia)

        if tecla in coordenadas:
            gamelib.play_sound('sound/stepstone_1.wav')
            grilla, movimientos, guia = realizar_movimiento(grilla, movimientos, tecla, guia)


gamelib.init(main)