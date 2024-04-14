"""Este archivo contiene las reglas para que el juego funcione correctamente, 
como lo es la deteccion de colision con los bordes o con las paletas de los 
jugadores y la deteccion de puntos"""

def detec_colision_bordes(pelota):
    """Esta funcion detecta si la pelota va a superar el limite establecido 
    de la ventana y cambia su direccion"""
    if pelota.ycor() > 290 or pelota.ycor() < -290:
        pelota.dy *= -1


def detec_colision_paletas(pelota, paleta1, paleta2):
    """Esta funcion detecta si la pelota hace contacto con alguna de las
    las paletas, lo hace verificando si la pelota tiene una posicion cercana 
    a la paleta en el eje X y en el eje Y, al detectar una colision cambia la
    direccion de la pelota"""
    if ((-350 < pelota.xcor() < -340) and (paleta1.ycor() + 50 >= pelota.ycor() >= paleta1.ycor() - 50)) or \
        ((350 > pelota.xcor() > 340) and (paleta2.ycor() + 50 >= pelota.ycor() >= paleta2.ycor() - 50)):
            pelota.dx *= -1


def detec_puntos(pelota, puntajes, jugador1, jugador2):
    """Esta funcion detecta si ha habido un punto, si hay un punto se añade al
    jugador correspondiente y la pelota regresa a su sitio, se cambia su color
    mientras va de regreso para que parezca que se creo una nueva pelota.
    La funcion devuelve un valor booleano para que si hay un punto en el codigo
    principal se actualice el marcador"""
    if pelota.xcor() < -405:
        pelota.color("black")
        pelota.goto(0,0)
        pelota.color("white")
        pelota.dx *= 1
        puntajes[jugador2] += 1
        return True
    elif pelota.xcor() > 405:
        pelota.color("black")
        pelota.goto(0,0)
        pelota.color("white")
        pelota.dx *= 1
        puntajes[jugador1] += 1
        return True
    return False
