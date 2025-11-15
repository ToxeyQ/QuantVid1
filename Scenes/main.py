from manim import *



class GridRectangle(VGroup):
    """
    A reusable rectangle divided into rows x columns.
    Example:
        GridRectangle(rows=2, cols=1)
        GridRectangle(rows=3, cols=2, width=6, height=3)
    """

    def __init__(self, rows=2, cols=1, width=6, height=3, rect_color=WHITE, line_color=WHITE, **kwargs):
        super().__init__(**kwargs)

        # Main rectangle
        rect = Rectangle(width=width, height=height, color=rect_color)
        self.add(rect)

        # Vertical lines
        for c in range(1, cols):
            x = -width/2 + c * width / cols
            line = Line(start=rect.get_bottom() + RIGHT*(x+width/2),
                        end=rect.get_top() + RIGHT*(x+width/2),
                        color=line_color)
            self.add(line)

        # Horizontal lines
        for r in range(1, rows):
            y = -height/2 + r * height / rows
            line = Line(start=rect.get_left() + UP*(y+height/2),
                        end=rect.get_right() + UP*(y+height/2),
                        color=line_color)
            self.add(line)

        # Store rows and cols for reference
        self.rows = rows
        self.cols = cols
        self.rect = rect

class Demo(Scene):
    def construct(self):
        # Create the main rectangle
        rect = Rectangle(width=6, height=3, color=WHITE)
        rect.move_to(ORIGIN)
        
        # Create the vertical line (2x1 grid)
        vertical_line = Line(
            start=rect.get_top(),
            end=rect.get_bottom()
        ).move_to(rect.get_center())
        
        # Draw the diagonal line: bottom-left corner to top center
        bottom_left = rect.get_corner(DL)
        diagonal = Line(start=bottom_left, end=rect.get_top())
        
        # Fill the areas using polygons
        top_polygon = Polygon(
            rect.get_top(),                 
            rect.get_top() + LEFT*rect.width/2,  
            bottom_left,                    
            color=RED,
            fill_opacity=0.5
        )
        
        bottom_polygon = Polygon(
            bottom_left,
            rect.get_bottom() + RIGHT*rect.width/2, 
            rect.get_bottom() + RIGHT*rect.width/2 + UP*rect.height,  
            rect.get_bottom() + UP*rect.height + LEFT*0,  
            color=GREEN,
            fill_opacity=0.5
        )
        
        # Create labels
        label_a = MathTex("a").next_to(rect.get_left(), LEFT)
        label_b = MathTex("b").next_to(rect.get_bottom() +  LEFT*rect.width/5, DOWN)
        
        label_y1 = MathTex("1").next_to(rect.get_bottom() ,DOWN)
        label_y2 = MathTex("2").next_to(rect.get_bottom() + RIGHT*rect.width/2, DOWN)

        label_x1 = MathTex("1").next_to(rect.get_corner(DL) + UP * rect.height ,LEFT)


        # Animate everything
        self.play(Create(rect), Create(label_y1), Create(label_y2), Create(label_x1))
        self.wait(3)
        self.play(Create(vertical_line))
        self.wait(3)
        self.play(Write(label_a), Write(label_b))

        self.play(Create(diagonal))
        self.wait(3)
        self.play(FadeIn(top_polygon), FadeIn(bottom_polygon))
        self.wait(3)
