# Importing the turtle  

import turtle as trtl  

   

# creating the turtle as an object  

painter = trtl.Turtle()  

   

#coloring the smiley face  

color = input("What color do you want your smiley face to be?")  

painter.fillcolor(color)  

painter.begin_fill()  

   

#drawing the main face shape  

painter.penup()  

painter.goto(0,-90)  

painter.pendown()  

painter.pensize(5)  

painter.circle(150)  

   

painter.end_fill()  

   

#drawing eye 1  

painter.penup()  

painter.goto(-90,100)  

painter.pendown()  

   

painter.right(130)  

painter.circle(50, -90, 2)  

   

# drwaing eye 2  

painter.penup()  

painter.goto(40,100)  

painter.pendown()  

   

painter.left(90)  

painter.circle(50, -90, 2)  

   

#coloring the mouth  

mouth = "brown"  

painter.fillcolor(mouth)  

painter.begin_fill()  

   

#drawing the mouth  

painter.penup()  

painter.goto(-80, 20)  

painter.pendown()  

   

painter.right(140)  

painter.forward(180)  

   

painter.left(90)  

painter.circle(90, -180)  

   

painter.end_fill()  

   

# create screen object and make it persist  

wn = trtl.Screen()  

wn.mainloop()  


