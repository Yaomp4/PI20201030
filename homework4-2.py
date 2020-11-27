import turtle
qwer=turtle.Turtle()
qwer.color('green')
qwer.shape('turtle')
qwer.stamp()
qwer.penup()

r=5
i=1
for i in range(25):
    
  
    qwer.circle(r,i+15)
    qwer.stamp()
    qwer.penup()
    qwer.right(90)
    qwer.forward(50)
    qwer.left(90)

    i=i+5
    


