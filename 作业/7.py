import turtle

pen = turtle.Pen()

colors=['red','pink','blue','green','yellow','orange','cyan','magenta','aquamarine']
pen.setx(-100)
pen.pensize(10)
for color in colors:

    pen.color(color)
    print(color)
    pen.forward(100)

turtle.done()
