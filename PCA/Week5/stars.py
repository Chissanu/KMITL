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
    t.ht()
    y = (n * 50) + 100
    t.up()
    t.goto(-400,y)
    t.down()
    for i in range(n):
        t.dot(20)
        t.up()
        t.fd(50)
        t.down()
    if n > 1:
        draw1(n-1,t)
    y = (n * -50) + 150
    t.up()
    t.goto(-400,y)
    t.down()
    for i in range(n):
        t.dot(20)
        t.up()
        t.fd(50)
        t.down()

def draw2(n,t,num):
    t.ht()
    y = (n * 50) + 100
    t.up()
    t.goto(-400,y)
    t.down()
    if n <= 0:
        return
    else:
        for i in range(num):
            t.dot(20)
            t.up()
            t.fd(50)
            t.down()
        draw2(n-1,t,num+1)
        y = (n * -50) + 150
        t.up()
        t.goto(-400,y)
        t.down()
        for i in range(num):
            t.dot(20)
            t.up()
            t.fd(50)
            t.down()
            

def main():
    t = turtle.Turtle()
    turtle.bgcolor("light blue")
    t.speed(0)
    t.pensize(5)
    t.up()
    t.setpos(-400,350)
    t.down()
    #draw1(5,t)
    draw2(5,t,1)
    

#stars1(5)
main()
stars2(5,1)
turtle.exitonclick()