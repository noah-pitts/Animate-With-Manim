from manim import *


class CreateShapes(Scene):
    def construct(self):

        triangle = Triangle()  # create a triangle
        triangle.set_fill(BLUE, opacity=1)  # set the color and transparency
        self.play(Create(triangle))  # show the triangle on screen

        circle = Circle()  # create a circle
        circle.set_fill(RED, opacity=1)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

        square = Square()  # create a square
        square.set_fill(GREEN, opacity=1)  # set the color and transparency
        self.play(Create(square))  # show the square on screen

