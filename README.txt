// --- SOKOBAN --- //

Sokoban es un clásico rompecabezas inventado en Japón, normalmente implementado como videojuego. El juego original fue creado por Hiroyuki Imabayashi, que en 1980 ganó con su juego una competición contra un ordenador. Hiroyuki Imabayashi es presidente de la empresa Thinking Rabbit Inc. en Japón. Con los años han aparecido muchas versiones del juego para todas las plataformas, y continuamente se crean nuevas colecciones de niveles.

Sokoban significa "encargado de almacén" en japonés. El objetivo del juego es empujar las cajas (o las bolas) hasta su lugar correcto dentro de un reducido almacén, con el número mínimo de empujes y de pasos. Las cajas se pueden empujar solamente, y no tirar de ellas, y sólo se puede empujar una caja a la vez. Parece fácil, pero los niveles van desde muy fáciles a extremadamente difíciles, y algunos lleva horas e incluso días resolverlos. La simplicidad y la elegancia de las reglas han hecho de Sokoban uno de los juegos de ingenio más populares.

https://es.wikipedia.org/wiki/Sokoban

// --- DEPENDENCIAS --- //

Gamelib is a pure-Python single-file library/framework for writing simple games.
https://github.com/dessaya/python-gamelib

Incluido, aunque tambien puede consultar la ultima version.

// --- INICIAR --- //

python main.py

python3 main.py

// --- CONTROLES --- //

Flecha arriba o W = subir
Flecha izquierda o A = ir hacia la izquierda
Flecha abajo o S = bajar
Flecha derecha o D = ir hacia la derecha
R = reiniciar
Escape = salir
Z = deshacer
H = pista

// --- ACERCA DEL PROYECTO --- //

soko.py incluye las funciones necesarias para manejar la logica del juego.

backtraking.py incluye las funciones de backtracking, utilizadas para proporcionar pistas al jugador.

IMPORTANTE
A partir del nivel 5 utilizar pistas (H) produce el siguiente error:
RecursionError: maximum recursion depth exceeded while calling a Python object
Por seguridad python limita la cantidad de llamadas recursivas a 999, asi evita la recursion infinita para no hacer overflow en el stack de C.
La complejidad del nivel 5 ya es suficiente para superar este numero. Se podria deslimitar pero no tendria mucho sentido, el proyecto es puramente didactico.
(para mas informacion: https://docs.python.org/2/library/sys.html#sys.getrecursionlimit)

main.py integra los modulos antes mencionados, parsea los niveles, las teclas y renderiza el juego utilizando funciones del modulo gamelib.

Usted podria general sus propios niveles y agregarlos en el archivo niveles.txt:
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

    [
        '#####',
        '#.$ #',
        '#@  #',
        '#####',
    ]

Asegurese de utilizar el tipado correctamente siguiendo la estructura del resto de niveles.
Usted puede modificar el nivel inicial desde main.py en la linea 99.

// -- Mi Nombre -- //
// -- Sebastian M. Vintoñuke -- //

// -- Contacto -- //
// -- sebastian.m.vintonuke@gmail.com -- //
// -- https://github.com/SebastianVintonuke -- //
// -- https://www.linkedin.com/in/sebastian-vintoñuke-7ab06a161/ -- //