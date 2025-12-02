from manim import *
import numpy as np

class ExpectationFill(Scene):
    def construct(self):
        # Define axes
        axes = Axes(
            x_range=[0, 2.1, 0.2],
            y_range=[0, 2.4, 0.4],
            x_length=6,
            y_length=4,
            tips=False,
        )
        labels = axes.get_axis_labels("x", "f(x)")
        self.play(Create(axes), Write(labels))

        # Function
        f = lambda x: 2*x
        f2 = lambda x: 1

        graph = axes.plot(f, x_range=[0, 1], color=BLUE)
        graph2 = axes.plot(f2, x_range=[1, 2], color=BLUE)

        graph_label = axes.get_graph_label(graph, label="2x", x_val=1)
        self.play(Create(graph, graph2), FadeIn(graph_label))

        # Area under the curve – dynamic
        fill_tracker = ValueTracker(0)

        def get_area():
            return axes.get_area(
                graph,
                x_range=[0, fill_tracker.get_value()],
                color=YELLOW,
                opacity=0.5
            )

        area = always_redraw(get_area)
        self.add(area)

        # Expectation value as a function of the upper limit 'a'
        def expectation(a):
            if a == 0:
                return 0
            # Compute: E[X | 0 ≤ X ≤ a]
            if a < 1:

                num = (2/3) * a**3   # ∫ x·2x dx = ∫ 2x² dx = 2/3 a³
                den = a**2           # ∫ 2x dx = a²
            if a<=1:
                num  = 5
                den = 2
            
            return num / den     # = 2a/3

        # Dot at expectation value
        exp_dot = always_redraw(
            lambda: Dot(axes.c2p(expectation(fill_tracker.get_value()), 0), color=RED)
        )

        # Vertical line at expectation
        exp_line = always_redraw(
            lambda: axes.get_vertical_line(
                axes.c2p(expectation(fill_tracker.get_value()), f(expectation(fill_tracker.get_value()))),
                color=RED
            )
        )

        exp_label = always_redraw(
            lambda: Tex(
                r"E[X] = " + f"{expectation(fill_tracker.get_value()):.2f}"
            ).next_to(exp_line, UP)
        )

        self.play(FadeIn(exp_dot), FadeIn(exp_line), FadeIn(exp_label))

        # Animate filling: 0 → 0.5 → 1.0
        self.play(fill_tracker.animate.set_value(0.5), run_time=2)
        self.wait(0.5)
        self.play(fill_tracker.animate.set_value(1.0), run_time=2)

        self.wait(2)