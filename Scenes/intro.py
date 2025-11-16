from manim import *
""""
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



class QuantumIntro(Scene):
    def construct(self):

        # --- Name Text ---
        title = Text("TheQuantumQuant", font_size=90)
        title.to_edge(UP)

        # Shift it far to the left so it writes in from left
        title.shift(2* DOWN)

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

        # Shift curve far to the right so it draws in from the right
        curve.shift(6 * RIGHT)

        self.play(
            Write(title),   # moves into place while being written
            Create(curve, run_time=3),        # draws from right (because shifted)
            run_time=3
        )

        self.wait(2)
"""

class QuantumIntro(Scene):
    def construct(self):
        #THIS IS ITTTTT
        # Write the title normally
        title = Text("TheQuantumQuant", font_size=120)


        # Add title to screen
        #self.play(Write(title))
        #self.wait(0.5)


        # --- Make the Q's white-filled circles manually ---
        # Find indices of the Q's inside the text object
        # (Manim splits text into submobjects per glyph)
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

        # Shift curve far to the right so it draws in from the right
        curve.shift(6 * RIGHT)

        #self.play(
        #    Write(title),   # moves into place while being written
        #    Create(curve, run_time=3),        # draws from right (because shifted)
        #    run_time=3
        #)
        #self.play(FadeIn(white_overlays, pupils), run_time=0.5)

        """
        self.play(
            AnimationGroup(
                Write(title),
                Create(curve),
                FadeIn(white_overlays, pupils),
                run_time=3,
                lag_ratio=0.833  # roughly 2.5/3 to start overlays late
            )
        )
        """ 
        


        self.play(
            Write(title),
            Create(curve),
            run_time=3
        )

    # Start FadeIn 0.5s before the above finishes
        self.wait(2.5)  # wait 2.5s into the 3s animation
        self.play(FadeIn(white_overlays, pupils), run_time=0.5)
        # Fade them in so you see the effect
        #self.play(FadeIn(white_overlays, pupils), run_time=0.5)


        # Animate pupils and look at one of the Gaussian peaks
        self.play(pupils.animate.shift(LEFT*0.2), run_time=0.3)  # Slight pupil movement for effect
        self.play(pupils.animate.shift(RIGHT*0.2), run_time=0.4)  # Slight pupil movement for effect
        self.play(pupils[0].animate.shift(DOWN*0.3 + 0.1*RIGHT), pupils[1].animate.shift(LEFT*0.1 + DOWN* 0.3), run_time=0.4)  # Slight pupil movement for effect
        



        ball = Circle(radius=0.3, color=BLUE, fill_opacity=1)
        ball.move_to([2, -2, 0]) # example position, adjust as needed
        self.play(FadeIn(ball), FadeOut(curve), run_time=0.2)
        self.wait(1)