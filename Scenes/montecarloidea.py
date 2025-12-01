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
        initial_positions = [0,0,0,
                             
                             0,0]  #maybe use a diff start later
        dots = VGroup()
        for i, x in enumerate(initial_positions):
            dot = Dot(point=[left_x + x, 2-i, 0], color=WHITE)
            dots.add(dot)


        estimate = DecimalNumber(0, num_decimal_places=3)
        estimate_text = VGroup(Text("Estimate:"), estimate).arrange(RIGHT, buff=0.4)
        estimate_text.to_edge(RIGHT)


        #self.add(estimate_text)       
        self.play(*[Create(bar) for bar in bars], *[Write(label) for label in labels], *[Create(dot) for dot in dots], Write(estimate_text))
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
            [0.2,0.7,0.8,1.6,1.6],
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
        #testing = [0,0,0.5,0.4,0.3,0.35]  #For testing purposes


        #This whole section is to have the speedy effect, its highly customizable so check whats best!
        min_run_time = 0.01  # fastest speed
        max_run_time = 1.0   # slowest speed
        num_runs = len(runs)

        for run_idx, x_positions in enumerate(runs):
            # exponential decrease: run_time = min + (max - min) * exp(-k * idx)
            k = 0.3  #stiffness coeff customize!! 0.25 is aestetic but takes a while
            k2 = 0.3  #For second half different stiffness
            run_time = min_run_time + (max_run_time - min_run_time) * np.exp(-k2*run_idx) + (max_run_time - min_run_time-0.3) * np.exp(-k*(num_runs - run_idx))
            #if run_idx > num_runs - 5:  # slow down for the last 5 runs
            #    run_time = (run_idx - num_runs +6) * 0.1
            animations = []
            for i, x in enumerate(x_positions):
                new_x = np.clip(left_x + x, left_x, left_x + max_values[i])
                animations.append(dots[i].animate.move_to([new_x, 2-i, 0]))
            self.play(*animations, estimate.animate.set_value(run_idx), run_time=run_time)  #Replace with actual estimate value
            self.wait(0.08)  #Custom!!!! pause between runs (also a bit hardcoded whoops)


        #Also slow down for the last few but whatever

        self.wait(1)