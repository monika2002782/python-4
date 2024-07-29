#1
# import turtle
# wn = turtle.Screen()
# wn.bgcolor("light green")
# wn.title("Turtle")

# skk = turtle.Turtle()
# skk.forward(100)
# turtle.done()


#2

# # Python program to draw square  
# # using Turtle Programming 
# import turtle  
# skk = turtle.Turtle() 
  
# for i in range(4): 
#     skk.forward(50) 
#     skk.right(90) 
      
# turtle.done()


#3

# # Python program to draw star 
# # using Turtle Programming 
# import turtle 
# star = turtle.Turtle() 
  
# star.right(75) 
# star.forward(100) 
  
# for i in range(4): 
#     star.right(144) 
#     star.forward(100) 
      
# turtle.done()


#4

#  Python program to draw hexagon 
# using Turtle Programming 
# import turtle  
# polygon = turtle.Turtle() 
  
# num_sides = 6
# side_length = 70
# angle = 360.0 / num_sides  
  
# for i in range(num_sides): 
#     polygon.forward(side_length) 
#     polygon.right(angle) 
      
# turtle.done() 



#5

###parallelogram

# import turtle 
  
# # Initialize the turtle 
# t = turtle.Turtle() 
  
# # Set the turtle's speed 
# t.speed(1) 
  
# # Draw the parallelogram 
# for i in range(2): 
#     t.forward(100) 
#     t.left(60) 
#     t.forward(50) 
#     t.left(120) 
# turtle.done()


# #5
# import turtle 
  
# # Set up the turtle screen and set the background color to white 
# screen = turtle.Screen() 
# screen.bgcolor("white") 
  
# # Create a new turtle and set its speed to the fastest possible 
# pen = turtle.Turtle() 
# pen.speed(0) 
  
# # Set the fill color to red 
# pen.fillcolor("red") 
# pen.begin_fill() 
  
# # Draw the circle with a radius of 100 pixels 
# pen.circle(100) 
  
# # End the fill and stop drawing 
# pen.end_fill() 
# pen.hideturtle() 
  
# # Keep the turtle window open until it is manually closed 
# turtle.done() 

##6

# import turtle  #Inside_Out 
# wn = turtle.Screen() 
# wn.bgcolor("light green") 
# skk = turtle.Turtle() 
# skk.color("blue") 
  
# def sqrfunc(size): 
#     for i in range(4): 
#         skk.fd(size) 
#         skk.left(90) 
#         size = size + 5
  
# sqrfunc(6) 
# sqrfunc(26) 
# sqrfunc(46) 
# sqrfunc(66) 
# sqrfunc(86) 
# sqrfunc(106) 
# sqrfunc(126) 
# sqrfunc(146) 
# turtle.done()


###heart shape


# import turtle
# s = turtle.Screen()
# s.bgcolor('black')
# pen = turtle.Turtle()
# pen.speed(1)
# pen.color('red')
# pen.begin_fill()
# pen.fillcolor('red')
# pen.left(140)
# pen.forward(180)
# pen.circle(-90, 200)
# pen.setheading(60)
# pen.circle(-90, 200)
# pen.forward(180)
# pen.end_fill()
# pen.hideturtle()
# s.mainloop()



#####

# import turtle

# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
# t = turtle.Pen() 
# t.speed(0)
# turtle.bgcolor('black') 
# for x in range(360): 
# 	t.pencolor(colors[x%6]) 
# 	t.width(x//100 + 1) 
# 	t.forward(x) 
# 	t.left(90)
	
