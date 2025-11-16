from manim import *
import numpy as np


class QuantProblemVisualization(Scene):
    def construct(self):
        """
        This section first introduces the problem, then shows two examples ...
        """

        #Create text but mark letter so that it can be treated seperatly
        top_text = Text("Given 5 random variables:")
        a_text = MathTex(r"a \sim \text{Uniform}[0,1]", substrings_to_isolate=["a"])
        b_text = MathTex(r"b \sim \text{Uniform}[0,2]", substrings_to_isolate=["b"])
        c_text = MathTex(r"c \sim \text{Uniform}[0,3]", substrings_to_isolate=["c"])
        d_text = MathTex(r"d \sim \text{Uniform}[0,4]", substrings_to_isolate=["d"])
        e_text = MathTex(r"e", r"\sim \text{Uniform}[0,5]")     #best way to handle this bs
        bottom_text = Text("What is the probability that a < b < c < d < e ?")

        statement = VGroup(top_text,a_text, b_text, c_text, d_text, e_text, bottom_text)


        statement.arrange(DOWN, buff=0.5).to_edge(UP)
        #self.play(*[Write(s) for s in statement])
        #self.play(Write(statement), run_time=6)

        for i, state in enumerate(statement):

            if i == 0:
                time = 2.3
            if i == 6:  
                time = 3.3
            else:
                time = 1
            self.play(Write(state), run_time=time)
            self.wait(0.2)
        #self.play(Write(statement[0]), run_time=3)

        #self.play(Write(statement[1:6]), run_time=3)
        #self.play(Write(statement[6]), run_time=2)

        self.wait(1) 



        variables = ["a","b","c","d","e"]
        max_values = [1,2,3,4,5]
        colors = [BLUE, GREEN, YELLOW, ORANGE, RED]

        bars = VGroup()
        labels = VGroup()
        left_x = -5  #Kinda arbitrary so maybe choose it better


        #Create the bars for the examples
        for i, (var, max_val, color) in enumerate(zip(variables, max_values, colors)):
            bar = Line(
                start=np.array([left_x, 2-i,0]),
                end=np.array([left_x + max_val, 2-i,0]),
                color=color, stroke_width=6
            )
            
            bars.add(bar)

            label = MathTex(var).next_to(bar, LEFT)
            labels.add(label)

        self.wait(0.5)

        letters_to_move = VGroup(
            a_text[0], 
            b_text[0],
            c_text[0],
            d_text[0],
            e_text[0]
        )

        self.play(*[Transform(letter, label) for letter, label in zip(letters_to_move, labels)], FadeOut(a_text[1],b_text[1],
            c_text[1],
            d_text[1],
            e_text[1]),[Create(bar) for bar in bars])
        
        

        self.wait(2)


        #inequality = MathTex("a < b < c < d < e").to_edge(DOWN)     #Not so nice rn change pos and timing 
        #self.play(Write(inequality))









        max_values = [1, 2, 3, 4, 5]


   
        x_pos_example_loss = [0.9,0.5,2,3.4,2.4]    #Chosen positions for a loss

        dots = VGroup()
        for i, max_val in enumerate(max_values):
            x_pos = x_pos_example_loss[i] + left_x
            dot = Dot(point=np.array([x_pos, 2-i, 0]), color=WHITE)
            dots.add(dot)
            self.play(FadeIn(dot), run_time=0.5)

        cross = Text("✗", font_size=200, color=RED)  
        cross.move_to(ORIGIN)



        self.play(dots[1].animate.set_color(RED), dots[4].animate.set_color(RED)) #Coloring problematic dots
        self.play(Write(cross.shift(RIGHT*3)))
        self.wait(1)
        self.play(FadeOut(cross, dots))




        x_pos_example_win = [0.5,1.2,2,3.4,4.5]     #Chosen positions for a win

        dots = VGroup()
        for i, max_val in enumerate(max_values):
            x_pos = x_pos_example_win[i] + left_x
            dot = Dot(point=np.array([x_pos, 2-i, 0]), color=WHITE)
            dots.add(dot)
            self.play(FadeIn(dot), run_time=0.5)

        check = MathTex(r"\checkmark")  
        check.set_color(GREEN)
        check.scale(6)



        self.play(Write(check.shift(RIGHT*3)))
        self.wait(2)
        self.play(FadeOut(check, bars, dots, letters_to_move, statement[0], statement[6]))  #Clear szene to continue


        final_text = Text("How do we continue from here")



