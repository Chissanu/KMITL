import turtle

def drawclock(r,hrs,length,color):
    turtle.pensize(10)
    turtle.penup()
    turtle.goto(0,r)
    turtle.pendown()
    turtle.pencolor("black")
    for degree in range(0,360,360//hrs):
        turtle.circle(-r,360//hrs)
        turtle.right(90)
        turtle.forward(length)
        turtle.back(length)
        turtle.left(90)
    for degree in range(0,360,360//60):
        turtle.circle(-r,360//60)
        turtle.right(90)
        turtle.forward(length/2)
        turtle.back(length/2)
        turtle.left(90)
    turtle.circle(-r)
    
def teleport(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
def drawHand(r,hour,min,sec):
    teleport(0,0)
    turtle.left(90)
    minT = (min * 6) + (sec * 0.3)
    hourT = (hour * 30) + (min * 0.6)
    secT = sec * 6

    turtle.pencolor("blue")
    turtle.right(minT)
    turtle.forward(150)
    turtle.home()
    # teleport(0,0)
    #Draw hour hand
    turtle.pencolor("red")
    turtle.left(90)
    turtle.right(hourT)
    turtle.forward(110)
    turtle.home()
    #Draw second hand
    turtle.pencolor("black")
    turtle.left(90)
    turtle.right(secT)
    turtle.forward(165)
    
    
def main():
    while True:
        turtle.speed(0)
        turtle.hideturtle()
        turtle.bgcolor("Light blue")
        turtle.title("Clock Face")
        drawclock(200,12,20,"cyan")
        resp = input("What time (HH:MM:SS)>")
        ans = resp.split(":")
        if len(ans) < 3 or len(ans) > 3:
            print("Missing/too many fields")
        ans = [int(numeric_string) for numeric_string in ans]
        if ans[0] > 24 or ans[0] < 0:
            print("Wrong hour format")
            break
        if ans[1] > 59 or ans[1] < 0 or ans[2] > 59 or ans[2] < 0:
            print("Wrong minutes/seconds format")
            break
            
        drawHand(200,ans[0],ans[1],ans[2])
        turtle.exitonclick()
        
main()

# Test Cases
# 2:30:45
# 17:45:25
# 25:04:24
# -5:05:22
# 5:-35:11
# 1:25:-2
