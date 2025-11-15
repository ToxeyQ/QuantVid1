from manim import *




class Demo(Scene):
    def construct(self):

        #Raw rectangle
        rect = Rectangle(width=6, height=3, color=WHITE)
        rect.move_to(ORIGIN)
        

        #"Creates" gridline 
        vertical_line = Line(
            start=rect.get_top(),
            end=rect.get_bottom()
        ).move_to(rect.get_center())
    

        #Split probabilties into win and loss regions
        bottom_left = rect.get_corner(DL)
        diagonal = Line(start=bottom_left, end=rect.get_top())
        

        #Coloring the two regions correspondingly
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
        
        #Labeling the Grid
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
