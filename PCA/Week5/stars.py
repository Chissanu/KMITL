import turtle

def stars1(n):
    print("*" * n)
    if n > 1:
        stars1(n - 1)
    print("*" * n)

def stars2(n,i):
    if n <= 0:
        return
    else:
        print("*" * i)
        stars2(n-1,i+1)
        print("*" * i)
        
# stars1(1)
# stars2(5,1)

def draw1(n,t):
    t.dot(20) 
    t.fd(100)
    print("*" * n)
    if n > 1:
        stars1(n - 1)
    print("*" * n)

def main():
    t = turtle.Turtle()
    turtle.bgcolor("light blue")
    t.speed(0)
    t.pensize(5)
    t.up()
    t.setpos(-400,350)
    t.down()
    draw(5,t)

main()
turtle.exitonclick()