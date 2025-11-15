from manim import *
import numpy as np


class QuantProblemVisualization(Scene):
    def construct(self):
        # --- Step 1: Problem statement ---
        # Split into separate MathTex for each variable
        a_text = MathTex(r"a \sim \text{Uniform}[0,1]", substrings_to_isolate=["a"])
        b_text = MathTex(r"b \sim \text{Uniform}[0,2]", substrings_to_isolate=["b"])
        c_text = MathTex(r"c \sim \text{Uniform}[0,3]", substrings_to_isolate=["c"])
        d_text = MathTex(r"d \sim \text{Uniform}[0,4]", substrings_to_isolate=["d"])
        e_text = MathTex(r"e", r"\sim \text{Uniform}[0,5]")     #best way to handle this bs
        statement = VGroup(a_text, b_text, c_text, d_text, e_text)
        statement.arrange(DOWN, buff=0.5).to_edge(UP)

        self.play(*[Write(s) for s in statement])
        self.wait(1)

        # --- Step 2: Create horizontal bars ---
        variables = ["a","b","c","d","e"]
        max_values = [1,2,3,4,5]
        colors = [BLUE, GREEN, YELLOW, ORANGE, RED]

        bars = VGroup()
        labels = VGroup()
        left_x = -5  # left endpoint

        for i, (var, max_val, color) in enumerate(zip(variables, max_values, colors)):
            bar = Line(
                start=np.array([left_x, 2-i,0]),
                end=np.array([left_x + max_val, 2-i,0]),
                color=color, stroke_width=6
            )
            
            bars.add(bar)

            # Empty label placeholder
            label = MathTex(var).next_to(bar, LEFT)
            labels.add(label)

        #self.play(*[Create(bar) for bar in bars])
        self.wait(0.5)

        # --- Step 3: Transform letters to labels ---
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
        
        

        # --- Step 4: Fade out rest of the text ---
        self.wait(2)
        inequality = MathTex("a < b < c < d < e").to_edge(DOWN)
        self.play(Write(inequality))









        max_values = [1, 2, 3, 4, 5]
        left_x = -5  # This will be the x-coordinate of all left endpoints


   
        x_pos_example_loss = [0.9,0.5,2,3.4,2.4]

        dots = VGroup()
        for i, max_val in enumerate(max_values):
            x_pos = x_pos_example_loss[i] + left_x
            dot = Dot(point=np.array([x_pos, 2-i, 0]), color=WHITE)
            dots.add(dot)
            self.play(FadeIn(dot), run_time=0.5)



        cross = Text("✗", font_size=200, color=RED)  
        cross.move_to(ORIGIN)


        self.play(dots[1].animate.set_color(RED), dots[4].animate.set_color(RED)) #List false ref
        self.play(Write(cross.shift(RIGHT*3)))
        self.wait(1)
        self.play(FadeOut(cross, dots))




        x_pos_example_win = [0.5,1.2,2,3.4,4.5]
        dots = VGroup()
        for i, max_val in enumerate(max_values):
            # random position in the range
            x_pos = x_pos_example_win[i] + left_x
            dot = Dot(point=np.array([x_pos, 2-i, 0]), color=WHITE)
            dots.add(dot)
            self.play(FadeIn(dot), run_time=0.5)



        check = MathTex(r"\checkmark")  
        check.set_color(GREEN)
        check.scale(6)



        self.play(Write(check.shift(RIGHT*3)))

        self.wait(2)

        self.play(FadeOut(check, dots, inequality, bars, letters_to_move))


        final_text = Text("How do we continue from here")



