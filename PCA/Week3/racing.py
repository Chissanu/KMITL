import random
import turtle as tur

class Turtle:
    def __init__(self,color,speed,leap):
        self.color = color
        self.speed = speed
        self.leap = leap
        self.turtle = tur.Turtle()
        self.turtle.color(self.color)
        self.turtle.speed(self.speed)
        self.turtle.shape("turtle")
        self.turtle.width(5)
        self.turtle.shapesize(2)
    
    def getColor(self):
        return self.color
    
    def getSpeed(self):
        return self.speed
    
    def getLeap(self):
        return self.leap
    
    def getTurtle(self):
        return self.turtle

    def getPos(self):
        return self.turtle.pos()
    
    def setSpeed(self,speed):
        self.speed = speed
    
    def move(self):
        choice = random.randint(1,4)
        if choice == 1:
            self.turtle.fd(50)
        if choice == 2:
            self.turtle.left(random.randint(1,60))
            self.turtle.fd(50)
        if choice == 3:
            self.turtle.right(random.randint(1,60))
            self.turtle.fd(50)
        if choice == 4:
            self.turtle.back(50)
    
    
class RobotTurtle(Turtle):
    def __init__(self,color,speed,leap,energy):
        super().__init__(color,speed,leap)
        self.energy = energy
    
    def getEnergy(self):
        return self.energy
        
def teleport(x,y,t):
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()
    
def main():
    tur.bgcolor("light blue")
    tur.setworldcoordinates(-20, -20, 20, 20)
    colors = ["Red","light salmon","White smoke","Purple","White","Pink","Green","Grey"]
    #count = int(input("How many turtles? >"))
    #num = random.randint(1,count)
    #print(f"There are {num} turtles and {count-num} robotTurtle")
    
    tList = []
    rtList = []
    # #Creating normal turtles
    
    
    for i in range(20):
        tList.append(Turtle(random.choice(colors),random.randint(1,3),random.randint(1,100)))
    #for i in range(count - num):
    #    rtList.append(RobotTurtle(random.choice(colors),random.randint(1,3),random.randint(1,100),random.randint(1,100)))
    
    for t in tList:
        ogSpeed = t.getSpeed()
        t.setSpeed(0)
        print(t.getSpeed())
        
    while True:
        for turtle in tList:
            #print(turtle.getColor())
            turtle.move()
            print(turtle.getColor())
            print((turtle.getPos()[0]))
            if (turtle.getPos()[0]) > 400:
                print("Win")
                exit()
        
    tur.exitonclick()
    
    
    #print(tList)
    
    # t1 = Turtle("Blue",2,2)
    # t2 = Turtle("Red",2,5)
    # t3 = RobotTurtle("Cyan",2,2,6)


main()
