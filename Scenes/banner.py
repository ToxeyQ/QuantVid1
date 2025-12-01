
from manim import *


class QuantumIntro(Scene):
    def construct(self):
        title = Text("TheQuantumQuant", font_size=110)


        q_indices = [i for i, c in enumerate(title.text) if c == "Q"]


        # Add white circles over the Q glyphs
        white_overlays = VGroup()
        pupils = VGroup()
        for i in q_indices:
            q_mobj = title[i]
            # Create a circle matching the Q's size and position
            pupil = Circle(radius=0.1, color=BLACK, fill_opacity=1)
            overlay = Ellipse(width=1.0, height=1.1, color=WHITE, fill_opacity=1)
            overlay.move_to(q_mobj.get_center() + UP*0.12)    
            pupil.move_to(q_mobj.get_center() + UP*0.24+ RIGHT*0.1)


            white_overlays.add(overlay)
            pupils.add(pupil)


        # --- Double Gaussian Function ---
        def double_gauss(x):
            return (
                -1.2*np.exp(-(2*(x + 2)**2) / 1.2)
                - 1.2*np.exp(-(2*(x - 2)**2) / 1.2)
            )

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, -1.5, 0.5],
            x_length=10,
            y_length=2.5,
            tips=False
        )



        #axes.to_edge(DOWN)
        axes.next_to(title, DOWN, buff=0.5)
        axes.shift(LEFT*6)
        curve = axes.plot(double_gauss, color=BLUE)

        curve.shift(6 * RIGHT)



        self.play(
            LaggedStart(
            AnimationGroup(Write(title),Create(curve)),
            FadeIn(white_overlays, pupils),
            lag_ratio=0.833  # Start FadeIn 0.5s before the above finishes
            ),
            run_time=3
        )


        self.wait(2)
        #Add equations here
