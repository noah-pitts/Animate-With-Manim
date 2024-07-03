from manim import *

class hello(Scene):
    def construct(self):
        en_hello = Text("Hello!")
        esp_hello = Text("Hola!")
        self.play(Create(en_hello), run_time=2)
        self.wait(1)
        self.play(ReplacementTransform(en_hello,esp_hello))
        self.wait(3)