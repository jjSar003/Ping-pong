#Importar todas las funciones del modulo
from turtle import *
import objetos
import reglas
#Creacion de las funciones que permiten mover las paletas
"""Estas funciones son sencillas, se utilizaran para mover las paletas 
en base a ciertas teclas"""
def subir_paleta1():
    y = paleta1.ycor()
    y += 20
    paleta1.sety(y)
def bajar_paleta1():
    y = paleta1.ycor()
    y -= 20
    paleta1.sety(y)
def subir_paleta2():
    y = paleta2.ycor()
    y += 20
    paleta2.sety(y)
def bajar_paleta2():
    y = paleta2.ycor()
    y -= 20
    paleta2.sety(y)

#Importamos la ventana del archivo objetos
ventana = objetos.ventana(subir_paleta1, bajar_paleta1, subir_paleta2, bajar_paleta2)

#Pedimos el nombre de los jugadores
jugador1 = input("Introduce el nombre del jugador 1: ")
jugador2 = input("Introduce el nombre del jugador 2: ")

#Importamos el marcador del archivo objetos
marcador = objetos.marcador(jugador1, jugador2)

#Importamos las paletas del archivo objetos
paleta1 = objetos.paleta1()
paleta2 = objetos.paleta2()

#Importamos la pelota del archivo objetos
pelota = objetos.pelota()

#Creacion de un diccionario que contenga los puntajes 
puntajes = {jugador1: 0,
            jugador2: 0}

#El bucle permite hacer el juego interactivo
while True:
    #Con esta funcion podemos mostrar interactivamente las acciones
    ventana.update()
    #Con estas lineas hacemos que la pelota se mueva en cada iteracion del bucle
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
    #Importamos la funcion que cambia la direccion de la pelota si llega a
    #tocar un borde
    reglas.detec_colision_bordes(pelota)
    #Importamos la funcion que detecta si la pelota hace contacto con una paleta
    reglas.detec_colision_paletas(pelota, paleta1, paleta2)
    #Importamos la funcion que detecta si ha habido un punto y llama a la 
    #funcion que actualiza el marcador
    anotacion = reglas.detec_puntos(pelota, puntajes, jugador1, jugador2)
    if anotacion:
        marcador_actualizado = objetos.actualizar_marcador(marcador, puntajes, jugador1, jugador2)
    #Verificamos si algun jugador tiene 3 puntos, guardamos su nombre en una
    #variable y salimos del bucle
    if puntajes[jugador1] == 3:
        ganador = jugador1
        break
    elif puntajes[jugador2] == 3:
        ganador = jugador2
        break

#Importamos la ventana del juego final 
pantalla_fin_juego, ventana = objetos.mostrar_fin_juego(ganador, ventana, puntajes, jugador1, jugador2)
#Con esta funcion mantenemos la ventana a la vista hasta que le usuario haga click
exitonclick()