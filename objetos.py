from turtle import *
"""Este archivo contiene los objetos que requiere script principal para 
funcionar. Como lo es la ventana, el marcador, la pelota, las dos paletas y la
pantalla de fin del juego."""
def ventana(subir1, bajar1, subir2, bajar2):
    """Esta funcion crea la pantalla para la ejecucion del juego e 
    implementamos las teclas que permiten mover las paletas.
    Como parametro recibe las funciones que cambian la posicion de las paletas
    y devuelve la ventana para ser ejecutada en el script principal"""
    ventana = Screen()
    ventana.title("Ping Pong")
    ventana.bgcolor("black")
    ventana.setup(800, 600)
    ventana.listen()
    ventana.onkeypress(subir1, "w")
    ventana.onkeypress(bajar1, "s")
    ventana.onkeypress(subir2, "Up")
    ventana.onkeypress(bajar2, "Down")
    return ventana


def pelota():
    """Esta funcion crea la pelota del juego"""
    pelota = Turtle()
    pelota.shape("circle")
    pelota.color("white")
    pelota.penup()
    pelota.goto(0, 0)
    pelota.dx = 2
    pelota.dy = -2
    return pelota


def paleta1():
    """Esta funcion crea la paleta del jugador 1"""
    paleta1 = Turtle()
    paleta1.shape("square")
    paleta1.color("white")
    paleta1.shapesize(stretch_wid = 5, stretch_len=1)
    paleta1.penup()
    paleta1.goto(-350, 0)
    return paleta1


def paleta2():
    """Esta funcion crea la paleta del jugador 2"""
    paleta2 = Turtle()
    paleta2.shape("square")
    paleta2.color("white")
    paleta2.shapesize(stretch_wid = 5, stretch_len=1)
    paleta2.penup()
    paleta2.goto(350, 0)
    return paleta2

def marcador(jugador1, jugador2):
    """Esta funcion crea el marcador"""
    marcador = Turtle()
    marcador.color("white")
    marcador.speed(0)
    marcador.penup()
    marcador.hideturtle()
    marcador.setposition(0, 250)
    marcador.write("{}: 0 | {}: 0".format(jugador1, jugador2), align="left", font=("Arial", 14, "normal"))
    return marcador

def actualizar_marcador(marcador, puntajes, jugador1, jugador2):
    """La funcion permite cambiar la informacion del marcador"""
    marcadorstring = "{} : {} | {} : {}".format(jugador1, puntajes[jugador1], jugador2, puntajes[jugador2])
    marcador.clear()
    marcador.write(marcadorstring, align="left", font=("Arial", 14, "normal"))
    return marcador

def mostrar_fin_juego(ganador, ventana, puntajes, jugador1, jugador2):
     """Esta funcion muestra la venta final del juego, con el nombre del 
     ganador"""
     ventana.bgcolor("white")
     fin_juego = Turtle()
     fin_juego.color("black")
     fin_juego.penup()
     fin_juego.hideturtle()
     fin_juego.goto(0, 200)
     fin_juego.write("{} es el ganador".format(ganador), align="center", font=("Arial", 30, "normal"))
     fin_juego.hideturtle()
     fin_juego.goto(0, 0)
     fin_juego.write("{} : {}".format(puntajes[jugador1], puntajes[jugador2]), align="center", font=("Arial", 30, "normal"))
     fin_juego.hideturtle()
     fin_juego.goto(0, -200)
     fin_juego.write("¡¡Felicidades!!", align="center", font=("Arial", 30, "normal"))
     return fin_juego, ventana