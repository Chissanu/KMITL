import turtle

def drawtree(length, n,t):
    if n >= length:
        return 1
    else:
        t.forward(length)
        t.lt(30)
        drawtree(length * 0.6, n,t)
        t.rt(60)
        drawtree(length * 0.6, n,t)
        t.lt(30)
        t.backward(length)

def main():
    t = turtle.Turtle()
    turtle.bgcolor("light blue")
    t.speed(0)
    t.pensize(5)
    t.up()
    t.backward(150)
    t.down()
    drawtree(126, 6,t)

main()
turtle.exitonclick()