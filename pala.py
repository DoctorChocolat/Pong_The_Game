from turtle import Turtle

class Pala (Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")  # Forma rectangular
        self.shapesize(stretch_wid=5, stretch_len=1)  # Ancho: 20, Alto: 100
        self.penup()  # Levanta el lápiz para mover la pala
        self.goto(position)  # Posición inicial (x_pos = 350, y_pos = 0)
        self.color("red")  # Color de la pala
        
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)