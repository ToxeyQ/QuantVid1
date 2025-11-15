from manim import *

class QuantumIntro(Scene):
    def construct(self):
        # Create the text
        title = Text("TheQuantumQuant", font_size=72, color=BLUE)
        title.move_to(ORIGIN)

        # Animate writing the text
        self.play(Write(title))

        # Add a slight bounce / scale effect
        self.play(title.animate.scale(1.2), run_time=0.5)
        self.play(title.animate.scale(1/1.2), run_time=0.5)

        # Add a color fade
        self.play(title.animate.set_color(YELLOW), run_time=1)
        self.play(title.animate.set_color(WHITE), run_time=1)

        # Hold the final frame
        self.wait(1)