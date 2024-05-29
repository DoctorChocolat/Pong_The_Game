import time
from turtle import Turtle, Screen
from pala import Pala
from ball import Ball
from scoreboard import Scoreboard

#Configuro pantalla
screen= Screen()
screen.setup(800, 600)
screen.bgcolor("green")
screen.title("PONG")
#screen.tracer(0)

#Dibujando linea de campo
linea = Turtle()
linea.color("white")  # Color de la línea
linea.pensize(10)
linea.speed(0)  # Velocidad máxima
linea.penup()
linea.goto(0, -300)  # Comienza en la parte inferior del centro
linea.pendown()
linea.goto(0, 300)   # Termina en la parte superior del centro
# Esconde el Turtle y muestra el resultado
linea.hideturtle()


pala_derecha = Pala ((350,0))
pala_izquierda = Pala ((-350,0))
ball  = Ball ((0,0))
scoreboard = Scoreboard()

# Escucha las teclas de flecha y letras. 
screen.listen()
screen.onkeypress(pala_derecha.go_up, "Up")  # Flecha arriba
screen.onkeypress(pala_derecha. go_down, "Down")  # Flecha abajo
screen.onkeypress(pala_izquierda.go_up, "w")  # w mueve hacia arriba
screen.onkeypress(pala_izquierda. go_down, "s")  # s mueve hacia abajo

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detectar la colision con los muros de arriba y abajo, como la ball empieza en 0,0 y la pantalla es de 600 tiene 300 px para arriba y 300 pix para abajo.
    if ball.ycor() > 280 or ball.ycor() < -280:
        #necesita rebotar
        ball.bounce_y()
    #Detecta colision con la pala_derecha
    if ball.distance(pala_derecha) < 50 and ball.xcor() > 320 or ball.distance(pala_izquierda) <50 and ball.xcor()< -320:
        ball.bounce_x()
    

    #Detecta si la bola sale por el lado derecho. Falla el jugador
    if ball.xcor() > 440:
        ball.reset_position()
        scoreboard.l_point()

    #Detecta si la bola sale por lado izquierdo. Falla el jugador
    if ball.xcor() < -440:
        ball.reset_position()
        scoreboard.r_point()
    




screen.exitonclick()