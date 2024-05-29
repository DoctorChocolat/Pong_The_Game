from turtle import Turtle

class Ball (Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("circle")  # Forma rectangular
        self.shapesize(stretch_wid=1, stretch_len=1)  # Ancho: 20, Alto: 20
        self.penup()  # Levanta el lápiz para mover la pala
        self.goto(position)  # Posición inicial (x_pos = 0, y_pos = 0)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
    def move (self):
        new_x = self.xcor() +  self.x_move #aumenta 10 pixeles
        new_y = self.ycor() +  self.y_move
        self.goto(new_x, new_y)

    def bounce_y (self): #rebote, invirte cooodernadas 10 * -1 = -10, muros de arriba y abajo
        self.y_move *= -1

    def bounce_x (self): #Rebote invierte en la coordenada X donde estan las palas
        self.x_move *= -1
        self.move_speed *= 0.7

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()

       