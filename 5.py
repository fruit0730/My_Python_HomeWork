#海龟作图
import random
import turtle




pen = turtle.Pen()
text = turtle.Pen()
text1=turtle.Pen()
colors=['red','pink','blue','green','yellow','orange','cyan','magenta','aquamarine']
try:
    pen.pensize(5)
    pen.speed(0)
    pen.left(45)

    text.hideturtle()
    text.up()
    text.goto(-200,200)

    text.pendown()

    text1.hideturtle()
    text1.penup()
    text1.goto(-200,200)
    text1.pendown()
    text1.write(f"线段长度：", move=False, align="left", font=("Arial", 10, "normal"))


    for i in range(1000000000):
        long=1+i
        text.write(f"线段长度：{long}", move=False, align="left", font=("Arial", 10, "normal"))

        pen.forward(long)
        pen.left(90)
        pen.color(random.choice(colors))
        text.clear()


    turtle.done()

except :
    print("结束")