from manim import *


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
        label_b = MathTex("b").next_to(rect.get_bottom() +  RIGHT*rect.width/5, DOWN)
        
        # Animate everything
        self.play(Create(rect), Create(vertical_line))
        self.play(Write(label_a), Write(label_b))

        self.play(Create(diagonal))
        self.play(FadeIn(top_polygon), FadeIn(bottom_polygon))
        self.wait(3)