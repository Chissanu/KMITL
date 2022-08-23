import random
import turtle as tur

class Turtle:
    def __init__(self,color):
        self.color = color
        self.turtle = tur.Turtle()
        self.turtle.ht()
        self.turtle.color(self.color)
        self.turtle.shape("turtle")
        self.turtle.width(5)
        self.turtle.pensize(2)
        self.turtle.shapesize(2)
    
    def getColor(self):
        return self.color
    
    def getTurtle(self):
        return self.turtle

    def getPos(self):
        return self.turtle.pos()
    
    def setSpeed(self,speed):
        self.speed = speed
    
    def move(self):
        choice = random.randint(1,2)
        speed = random.randint(1,3)
        leap = random.randint(10,20)  
        self.turtle.speed(speed)
        
        if choice == 1:
            self.turtle.fd(leap)
        if choice == 2:
            if self.turtle.pos()[0] < -400:
                self.turtle.goto(-400,self.turtle.pos()[1])
            else:
                self.turtle.back(leap - 8)
    
class RobotTurtle(Turtle):
    def __init__(self,color,energy):
        super().__init__(color)
        self.energy = energy
    
    def getEnergy(self):
        return self.energy
    
    def move(self):
        choice = random.randint(1,4)
        angle = random.randint(1,60)
        speed = random.randint(1,3)
        leap = random.randint(10,20)
        
        self.turtle.speed(speed)
        if self.energy > 0:
            if choice == 1:
                self.turtle.fd(leap)
            if choice == 2:
                if self.turtle.pos()[1] > 400:
                    self.turtle.goto(self.turtle.pos()[0],400)
                    self.turtle.right(90)
                else:
                    self.turtle.left(angle)
                    self.turtle.fd(leap + 20)
            if choice == 3:
                if self.turtle.pos()[1] < -400:
                    self.turtle.goto(self.turtle.pos()[0],-400)
                    self.turtle.left(90)
                else:
                    self.turtle.right(angle)
                    self.turtle.fd(leap)
            if choice == 4:
                if self.turtle.pos()[0] < -400:
                    self.turtle.goto(-400,self.turtle.pos()[1])
                else:
                    self.turtle.back(leap - 8)
            self.energy -= leap
            print(f"{self.color} energy is at {self.energy}")
            
        
def teleport(x,y,t):
    t.ht()
    t.speed(0)
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()
    t.st()
    
def main():
    tur.bgcolor("black")
    
    colors = ['red', 'green', 'blue', 'orange', 'yellow', 'grey', 'purple', 'pink', 'brown', 'cyan']
    
    count = input("How many turtles? (2-10)>")
    
    if count < 2 or count > 10:
        print("Invalid counts!")
        
    num = random.randint(1,count)
    print(f"There are {num} turtles and {count-num} robotTurtle")

    tList = []
    rtList = []
    
    #Creating normal turtles
    for i in range(num):
        color = random.choice(colors)
        colors.remove(color)
        t = Turtle(color)
        tList.append(t)
        
    #Creating robot turtles
    for i in range(count - num):
        color = random.choice(colors)
        energy = random.randint(1000,1500)
        colors.remove(color)
        rt = RobotTurtle(color,energy)
        rtList.append(rt)
    
    turtles = tList + rtList
    random.shuffle(turtles)
    
    point = 380
    grid = (400 / len(turtles)*2)
    for t in turtles:
        teleport(-450,point,t.getTurtle())
        point -= grid
        
    while True:
        win = False
        for turtle in turtles:
            turtle.move()
            if (turtle.getPos()[0]) > 450:
                win = turtle.getColor() + " wins!"
                print(win)
                break
            if len(rtList) == len(turtles):
                num = 0
                for rt in rtList:
                    num += rt.getEnergy()
                if num < 0:
                    print("No energy left")
                    break
        if win != "" and win != False:
            winT = tur.Turtle()
            winT.up()
            winT.setposition(-100,0)
            winT.down()
            winT.color("light blue")
            winT.write(win, font=("Verdana",35, "normal"))
            winT.ht()
            break
    tur.exitonclick()
    
main()

