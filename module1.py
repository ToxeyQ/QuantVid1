from manim import *
import numpy as np
from scipy.integrate import quad


# ============================================================
#   PiecewisePDF CLASS (REUSABLE)
# ============================================================

class PiecewisePDF:
    def __init__(self, axes, pieces, color=BLUE):
        """
        pieces: list of dicts:
            [
                {"func": lambda x: ..., "range": (a, b)},
                ...
            ]
        """

        self.axes = axes
        self.pieces = pieces
        self.color = color
        self.graphs = self._build_graphs()

    def _build_graphs(self):
        """Build Manim graph segments for each piece."""
        graphs = []
        for piece in self.pieces:
            a, b = piece["range"]
            g = self.axes.plot(piece["func"], x_range=[a, b], color=self.color)
            graphs.append(g)
        return graphs

    # ----------------------------------------------------

    def pdf(self, x):
        """Unified piecewise function."""
        for piece in self.pieces:
            a, b = piece["range"]
            if a <= x <= b:
                return piece["func"](x)
        return 0

    # ----------------------------------------------------

    def shade_up_to(self, t, fill_color=YELLOW, opacity=0.5):
        """Return VGroup areas under the curve for all pieces up to t."""
        shaded = VGroup()

        for graph, piece in zip(self.graphs, self.pieces):
            a, b = piece["range"]

            if t <= a:
                continue

            upper = min(t, b)
            shaded.add(
                self.axes.get_area(
                    graph,
                    x_range=[a, upper],
                    color=fill_color,
                    opacity=opacity
                )
            )

        return shaded

    # ----------------------------------------------------

    def integrate(self, func, t):
        """Generic piecewise integration of func(x)."""
        total = 0
        for piece in self.pieces:
            a, b = piece["range"]

            if t <= a:
                break

            upper = min(t, b)
            f_piece = piece["func"]

            # Integrate func(x, f_piece) over this piece
            val, _ = quad(lambda x: func(x, f_piece), a, upper)
            total += val

        return total

    # ----------------------------------------------------

    def numerator(self, t):
        """ ∫ x f(x) dx """
        return self.integrate(lambda x, f: x * f(x), t)

    def denominator(self, t):
        """ ∫ f(x) dx """
        return self.integrate(lambda x, f: f(x), t)

    # ----------------------------------------------------

    def expectation(self, t):
        den = self.denominator(t)
        if den == 0:
            return 0
        return self.numerator(t) / den

    # ----------------------------------------------------

    def domain(self):
        """Return (min_x, max_x)."""
        return self.pieces[0]["range"][0], self.pieces[-1]["range"][1]


# ============================================================
#   SCENE USING THE CLASS
# ============================================================

class ModularExpectationExample(Scene):
    def construct(self):
        
        # -----------------------
        # AXES
        # -----------------------
        axes = Axes(
            x_range=[0, 1.1, 0.2],
            y_range=[0, 2.2, 0.4],
            x_length=6,
            y_length=4,
            tips=False,
        ).shift(LEFT * 2)

        self.play(Create(axes), run_time=1)

        # -----------------------
        # PIECEWISE FUNCTION
        # Example:
        # f(x) = 2x,     0 ≤ x ≤ 0.5
        # f(x) = 1,      0.5 < x ≤ 1
        # -----------------------
        pieces = [
            {"func": lambda x: 2*x, "range": (0, 0.5)},
            {"func": lambda x: 2*x,   "range": (0.5, 1)},
        ]

        pdf = PiecewisePDF(axes, pieces, color=BLUE)

        # Graph drawing
        for g in pdf.graphs:
            self.play(Create(g), run_time=0.5)

        # Tracker for shading
        t = ValueTracker(0)
        xmin, xmax = pdf.domain()

        shaded = always_redraw(lambda: pdf.shade_up_to(t.get_value()))
        self.add(shaded)

        # -----------------------
        # EXPECTATION MARKERS
        # -----------------------
        exp_dot = always_redraw(
            lambda: Dot(
                axes.c2p(pdf.expectation(t.get_value()), 0),
                color=RED
            )
        )

        exp_line = always_redraw(
            lambda: axes.get_vertical_line(
                axes.c2p(pdf.expectation(t.get_value()),
                        pdf.pdf(pdf.expectation(t.get_value()))),
                color=RED
            )
        )
        exp_label = always_redraw(
            lambda: Text(
                "fasd",axes.c2p(pdf.expectation(t.get_value()), 0)
            )
         )



        self.play(FadeIn(exp_dot), FadeIn(exp_line), FadeIn(exp_label))

        # -----------------------
        # Animate sweep
        # -----------------------
        self.play(t.animate.set_value(xmax), run_time=4)

        self.wait(2)