from manim import *


class Demo(Scene):
    def construct(self):

        variables = ["a","b","c","d","e"]
        max_values = [1,2,3,4,5]
        colors = [BLUE, GREEN, YELLOW, ORANGE, RED]
        left_x = -5

        bars = VGroup()
        labels = VGroup()
        for i, (var, max_val, color) in enumerate(zip(variables, max_values, colors)):
            bar = Line(start=[left_x, 2-i, 0], end=[left_x+max_val, 2-i, 0], color=color, stroke_width=6)
            bars.add(bar)
            label = MathTex(var).next_to(bar, LEFT)
            labels.add(label)

        self.play(*[Create(bar) for bar in bars], *[Write(label) for label in labels])
        self.wait(0.5)

        initial_positions = [0,0,0,0,0]  #maybe use a diff start later
        dots = VGroup()
        for i, x in enumerate(initial_positions):
            dot = Dot(point=[left_x + x, 2-i, 0], color=WHITE)
            dots.add(dot)
            self.add(dot)  
        self.wait(0.5)


        #Probably better to randomly generate these but eeh
        runs = [
            [0.2,0.5,1.5,2.2,2.1],
            [0.7,1.0,2.0,3.0,4.0],
            [0.1,0.8,1.8,1.5,1.5],
            [0.5,1.2,0.2,3.1,4.2],
            [0.3,0.6,1.6,2.8,3.8],
            [0.8,1.5,2.5,0.7,2.5],
            [0.0,0.9,0.7,1.9,4.0],
            [0.4,1.0,2.0,3.0,2.0],
            [0.6,1.3,2.3,3.5,4.2],
            [0.2,0.7,0.8,2.6,0.6],
            [0.2,0.5,1.5,2.2,3.1],
            [0.7,1.0,2.0,3.0,1.0],
            [0.1,0.8,0.8,2.5,3.5],
            [0.5,1.2,2.2,1.1,4.2],
            [0.3,0.6,1.6,2.8,1.8],
            [0.8,1.5,0.5,1.7,4.5],
            [0.0,0.9,1.7,2.9,3.0],
            [0.4,1.0,0.0,0.0,4.0],
            [0.6,1.3,2.3,3.5,2.2],
            [0.2,0.7,0.8,1.6,1.6]
        ]



        #This whole section is to have the speedy effect, its highly customizable so check whats best!
        min_run_time = 0.01  # fastest speed
        max_run_time = 1.0   # slowest speed
        num_runs = len(runs)

        for run_idx, x_positions in enumerate(runs):
            # exponential decrease: run_time = min + (max - min) * exp(-k * idx)
            k = 0.25  #stiffness coeff customize!! 0.25 is aestetic but takes a while
            run_time = min_run_time + (max_run_time - min_run_time) * np.exp(-k*run_idx)

            animations = []
            for i, x in enumerate(x_positions):
                new_x = np.clip(left_x + x, left_x, left_x + max_values[i])
                animations.append(dots[i].animate.move_to([new_x, 2-i, 0]))
            self.play(*animations, run_time=run_time)
            self.wait(0.1)  #Custom!!!! pause between runs (also a bit hardcoded whoops)


        #Also slow down for the last few but whatever

        self.wait(1)