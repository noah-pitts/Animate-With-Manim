from manim import *

class hello(Scene):
    def construct(self):
        en_hello = Text("Hello")
        esp_hello = Text("Hola")
        self.play(Write(en_hello))
        self.wait(3)