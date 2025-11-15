from manim import *

class AnimateLetters(Scene):
    def construct(self):


        #Splice text!!!!!!!

        # Create a text object, isolating each letter as a sub-mobject
        mathTex0 = MathTex(r"x = \sum_{ g \in G } \left( x_{ g } \, g \right)")        
        #mathTex0[1].set_color(YELLOW)
        #mathTex0[3].set_color(YELLOW)
        #mathTex0[5].set_color(YELLOW)

        mathTex0 = MathTex(r"e \sim \text{Uniform}[0,5]")
        #self.play(Create(mathTex0))

        mathTex0 = MathTex(
            r"x_0 = \sum_{g_0 \in G_0} \left( x_1 g_1 \right) x_0",
            substrings_to_isolate=["x_0","g_0","G_0","x_1","g_1"]
        )
        self.play(Create(mathTex0))
        self.play(Create(mathTex0[0]))

        #self.play(Create(mathTex0))