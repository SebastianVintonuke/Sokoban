import soko

def buscar_solucion(estado_inicial):
    """Inicializa el diccionario de movimientos visitados"""
    visitados = {}
    return backtrack(estado_inicial, visitados)

def backtrack(estado, visitados):
    """Recibe un estado y un diccionario vacio. Devuelve True y una cola de movimientos solución o False y None"""
    visitados[str(estado)] = None
    if soko.juego_ganado(estado):
        # ¡encontramos la solución!
        return True, []
    for accion in acciones_posibles(estado):
        nuevo_estado = soko.mover(estado, accion)
        if str(nuevo_estado) in visitados:
            continue
        solución_encontrada, acciones = backtrack(nuevo_estado, visitados)
        if solución_encontrada:
            acciones.append(accion)
            return True, acciones
    return False, None

def acciones_posibles(estado):
    """Recibe un estado y devuelve todas las acciones posibles"""
    acciones_posibles = []
    direcciones = ((-1, 0),(1, 0),(0, -1),(0, 1))
    for direccion in direcciones:
        if soko.mover(estado, direccion) != estado:
            acciones_posibles.append(direccion)
    return acciones_posibles