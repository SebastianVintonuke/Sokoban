def crear_grilla(desc):
    '''Crea una grilla a partir de la descripción del estado inicial.

    La descripción es una lista de cadenas, cada cadena representa una
    fila y cada caracter una celda. Los caracteres pueden ser los siguientes:

    Caracter  Contenido de la celda
    --------  ---------------------
           #  Pared
           $  Caja
           @  Jugador
           .  Objetivo
           *  Objetivo + Caja
           +  Objetivo + Jugador

    Ejemplo:

    >>> crear_grilla([
        '#####',
        '#.$ #',
        '#@  #',
        '#####',
    ])
    '''
    grilla = []
    fila = []
    for cadena in desc:
        for caracter in cadena:
            if caracter in "#$@.* +":
                fila.append(caracter)
        grilla.append(fila)
        fila = []
    return grilla

def dimensiones(grilla):
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla.'''
    return(len(grilla[0]),len(grilla))

def hay_pared(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f).'''
    return grilla[f][c] == "#"

def hay_objetivo(grilla, c, f):
    '''Devuelve True si hay un objetivo en la columna y fila (c, f).'''
    return grilla[f][c] in ".*+"

def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f).'''
    return grilla[f][c] in "$*"

def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f).'''
    return grilla[f][c] in "@+"

def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''
    for fila in grilla:
        if "." in fila or "+" in fila:
            return False
    return True

def busca_jugador(grilla):
    """Devuelve una tupla con la posición del jugador en la columna y fila de la grilla."""
    dimension = dimensiones(grilla)
    for f in range (0,dimension[1]):
        for c in range (0,dimension[0]):
            if hay_jugador(grilla, c, f):
                return (c, f)

def mover(grilla, direccion):
    '''Mueve el jugador en la dirección indicada.

    La dirección es una tupla con el movimiento horizontal y vertical. Dado que
    no se permite el movimiento diagonal, la dirección puede ser una de cuatro
    posibilidades:

    direccion  significado
    ---------  -----------
    (-1, 0)    Oeste
    (1, 0)     Este
    (0, -1)    Norte
    (0, 1)     Sur

    La función debe devolver una grilla representando el estado siguiente al
    movimiento efectuado. La grilla recibida NO se modifica; es decir, en caso
    de que el movimiento sea válido, la función devuelve una nueva grilla.
    '''
    grilla_movida = [lista[:] for lista in grilla]
    posicion_jugador = busca_jugador(grilla)
    posicion_deseada = (posicion_jugador[0]+direccion[0],posicion_jugador[1]+direccion[1])
    posicion_deseada_2 = (posicion_deseada[0]+direccion[0],posicion_deseada[1]+direccion[1])
    if hay_pared(grilla, posicion_deseada[0], posicion_deseada[1]):
        return grilla_movida
    if hay_caja(grilla, posicion_deseada[0], posicion_deseada[1]):
        if hay_pared(grilla, posicion_deseada_2[0], posicion_deseada_2[1]):
            return grilla_movida
        if hay_caja(grilla, posicion_deseada_2[0], posicion_deseada_2[1]):
            return grilla_movida
        if hay_objetivo(grilla, posicion_deseada_2[0], posicion_deseada_2[1]):
            grilla_movida[posicion_deseada_2[1]][posicion_deseada_2[0]] = "*"
        else:
            grilla_movida[posicion_deseada_2[1]][posicion_deseada_2[0]] = "$"
    if hay_objetivo(grilla, posicion_deseada[0], posicion_deseada[1]):
        grilla_movida[posicion_deseada[1]][posicion_deseada[0]] = "+"
    else:
        grilla_movida[posicion_deseada[1]][posicion_deseada[0]] = "@"
    if hay_objetivo(grilla, posicion_jugador[0], posicion_jugador[1]):
        grilla_movida[posicion_jugador[1]][posicion_jugador[0]] = "."
    else:
        grilla_movida[posicion_jugador[1]][posicion_jugador[0]] = " "
    return grilla_movida

def historial(grilla, movimientos):
    """Recibe un estado de la grilla y una lista. Si la lista no tiene estados o el ultimo estado es diferente al estado actual, apila el nuevo estado"""
    if len(movimientos) == 0:
        movimientos.append(grilla)
    else:
        if grilla == movimientos[-1]:
            return movimientos
        movimientos.append(grilla)
    return movimientos

def deshacer(movimientos):
    """Recibe una lista de movimientos. Si hay más de un elemento borra y devuelve el ultimo, si no; devuelve el primero"""
    if len(movimientos) == 1:
        return movimientos[0]
    return movimientos.pop()