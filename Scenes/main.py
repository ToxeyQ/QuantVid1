from manim import *




class Demo(Scene):
    def construct(self):



        # Transition , probably best to add only in final scene, also transition is not the intro



        step1 = Text("Reduce the complexity of the problem", font_size=48)


        self.play(Write(step1))
        self.wait(1)
        self.play(FadeOut(step1))   
        

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



        self.play(FadeOut(rect, vertical_line, diagonal, label_a, label_b, label_y1, label_y2, label_x1, top_polygon, bottom_polygon))

        #Integral part

        #So what is the expectation value of b assuming a < b

        integral_text = Text("We can compute the expectation value of b if a < b:", font_size=36)

        integral_text.to_edge(UP)
        self.play(Write(integral_text))
        integral_eq = MathTex(r"E(b) = \int_{b_1}^{b_2} \rho (b) b db")
        integral_eq.next_to(integral_text, DOWN, buff=0.5)
        #Explain density function so also normalization, Also show how that comes to play, ie show that linear density
        integral_eq2 = MathTex(r"E(b) = \frac{2}{3}(\int_{0}^{1} b^2 db + \int_{1}^{2} b db)")
                
        integral_eq2.next_to(integral_eq, DOWN, buff=0.5)

        final_result = MathTex(r"E(b) = 11/9")


        self.play(Write(integral_eq))
        self.play(Write(integral_eq2))


        self.wait(3)
