import turtle

def teleport(x, y, t):
    t.ht()
    t.speed(0)
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()
    t.st()

def draw(length,t):
    if length < 100:
        return 1
    else:
        t.right(60)
        t.fd(length)
        t.left(120)
        return length * draw(length-1,t)
    
def main():
    t = turtle.Turtle()
    turtle.bgcolor("light blue")
    teleport(-450,0,t)
    t.fd(100)
    draw(500,t)

main()
turtle.exitonclick()