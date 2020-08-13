import turtle
circle=turtle.Turtle()
circle1=turtle.Turtle()
circle2=turtle.Turtle()
circle.shape("turtle")
circle1.shape("turtle")
circle2.shape("turtle")
circle.speed(10000)


#for first blue circle

def square(length,angle):
    for i in range(4):
        circle.forward(length)
        circle.right(angle)

for j in range(100):
    circle.color("blue")
    square(100,90)
    circle.right(11)
    


#for second red circle
    
circle1.speed(10000)
def square1(length,angle):
    for i in range(4):
        circle1.forward(length)
        circle1.right(angle)
        
for j in range(100):
    circle1.goto(x=-100,y=0)
    circle1.color("red")
    square1(100,90)
    circle1.right(11)


#for third green circle
    
circle2.speed(10000)
def square2(length,angle):
    for i in range(4):
        circle2.forward(length)
        circle2.right(angle)
        
for j in range(100):
    circle2.goto(x=100,y=0)
    circle2.color("green")
    square2(100,90)
    circle2.right(11)

#for thank you

circle.penup()
circle.goto(x=0,y=200)
circle.pendown()
circle.write("    THANK YOU :) " ,font=("bold"))





    
