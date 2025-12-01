from manim import *



class Probabilitydistributions(Scene):
    def construct(self):


        text = Text("Unnormalized Probability Distribution of b", font_size=48)  
        self.play(Write(text))
        self.play(text.animate.to_edge(UP))


        #Maybe put this in a function of like generate plot or something
        axes = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 1.2, 0.2],
            x_length=7,
            y_length=4,
            axis_config={"include_numbers": True},
        )

        axes_labels = axes.get_axis_labels(
            Text("b"), Text(r"p(b)")
        )

        # Piece 1: f(b)=b on (0,1)
        line1 = axes.plot(lambda b: b, x_range=[0, 1], color=BLUE)

        # Piece 2: f(b)=1 on (1,2)
        line2 = axes.plot(lambda b: 1, x_range=[1, 2], color=BLUE)

        # Vertical line at b=2 down to y=0
        vline = axes.get_vertical_line(axes.c2p(2, 0), color=RED)

        # Dot at (1,1) to close the corner
        dot = Dot(axes.c2p(1,1), color=BLUE)

        self.play(Create(axes), Write(axes_labels))
        self.play(Create(line1))
        self.play(Create(line2))
        self.play(Create(vline))
        self.play(FadeIn(dot))

        self.wait()

        self.play(FadeOut(axes, axes_labels, line1, line2, vline, dot))
        #Dont remove axis but transform it if its like here rn

                
        axes = Axes(
            x_range=[0, 3.5, 0.5],
            y_range=[0, 1.2, 0.2],
            x_length=7,
            y_length=4,
            axis_config={"include_numbers": True},
        )

        axes_labels = axes.get_axis_labels(
            Text("c"), Text(r"p(c")
        )

        # Piece 1: f(b)=b on (0,1)
        line1 = axes.plot(lambda b: 1/3*b**2, x_range=[0, 1], color=BLUE)

        # Piece 2: f(b)=1 on (1,2)
        line2 = axes.plot(lambda b: 2/3*b - 1/3, x_range=[1, 2], color=BLUE)


        line3 = axes.plot(lambda b: 1, x_range=[2,3], color=BLUE)
        # Vertical line at b=2 down to y=0
        vline = axes.get_vertical_line(axes.c2p(2, 0), color=RED)

        # Dot at (1,1) to close the corner 
        dot = Dot(axes.c2p(1,1), color=BLUE)

        self.play(Create(axes), Write(axes_labels))
        self.play(Create(line1))
        self.play(Create(line2))
        self.play(Create(line3))
        self.play(Create(vline))


