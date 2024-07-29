import turtle
m=turtle.Turtle()
m.color("cyan")
m.begin_fill()
m.circle(150)
m.end_fill()


#draw eye1
m.penup()
m.setposition(70,180)
m.pendown()
m.pencolor("black")
m.color("black")
m.pensize(0)
m.begin_fill()
m.speed(1)
m.right(90)
m.forward(10)
for i in range(145):
    m.right(1)
    m.forward(0.25)
m.right(30)
m.forward(30) 
for i in range(145):
    m.right(1)
    m.forward(0.25)
m.right(30)
m.forward(30)
m.end_fill()



#draw eye2
m.penup()
m.setposition(-30,180)
m.pendown()
m.pencolor("black")
m.color("black")
m.pensize(0)
m.begin_fill()
m.speed(1)
m.right(45)
m.forward(10)
for i in range(145):
    m.right(1)
    m.forward(0.25)
m.right(30)
m.forward(30) 
for i in range(145):
    m.right(1)
    m.forward(0.25)
m.right(30)
m.forward(30)
m.end_fill()


turtle.done()



