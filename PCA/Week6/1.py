import random
import turtle
class Line:
    def __init__(self, line):
        self.line = line

    def joinExtend(self,newLine):
        try:
            self.line.extend(newLine)
            return True
        except:
            return False
    
    def joinManual(self,newLine):
        try:
            self.line = self.line + newLine
            return True
        except:
            return False

    def zigzag1(self,newLine):
        line3 = []
        try:
            if len(self.line) > len(newLine):
                count = len(newLine)
            else:
                count = len(self.line)
            for i in range(count):
                line3.append(self.line.pop(0))
                line3.append(newLine.pop(0))
            line3.extend(self.line)
            line3.extend(newLine)
            self.line = []
            while newLine:
                line3.append(newLine.pop(0))
            return line3
        except:
            return False

    def zigzag2(self,newLine):
        tempLine = []
        try:
            if len(self.line) > len(newLine):
                count = len(newLine)
            else:
                count = len(self.line)
            for i in range(count):
                tempLine.append(self.line.pop(0))
                tempLine.append(newLine.pop(0))
            tempLine.extend(self.line)
            tempLine.extend(newLine)
            while newLine:
                tempLine.append(newLine.pop(0))
            self.line = tempLine
        except:
            pass
            
        
    def getLine(self):
        return self.line

    def printList(self):
        return self.line

    def __str__(self):
        return ', '.join(str(item) for item in self.line)

def console():
    points = []
    line1 = int(input("How many points for line1? >"))
    #Gen points Line1
    for i in range(line1):
        randx = random.randint(-line1,line1)
        randy = random.randint(-line1,line1)
        point = (randx,randy)
        points.append(point)
    line1 = Line(points)

    points = []
    line2 = int(input("How many points for line2? >"))
    #Gen points Line1
    for i in range(line2):
        randx = random.randint(-line2,line2)
        randy = random.randint(-line2,line2)
        point = (randx,randy)
        points.append(point)
    line2 = Line(points)

    #Ask for choice
    print("What do you want to do")
    print("\t1.Join")
    print("\t2.Join Zigzag1")
    print("\t3.Join Zigzag2")
    option = int(input("What do you want to do >"))
    #Join lines
    if option == 1:
        err = line1.joinExtend(line2.getLine())
        if err == True:
            line2 = []
        print(f"Line1 has: {line1}")
        print(f"Line2 has: {line2}")
    #Zigzag1
    elif option == 2:
        print(f"Line1 has: {line1}")
        print(f"Line2 has: {line2}")
        line3 = line1.zigzag1(line2.getLine())
        print("Completed")
        print(f"Line1 has: {line1}")
        print(f"Line2 has: {line2}")
        print(f"Line3 has: {line3}")
    #Zigzag2
    elif option == 3:
        print(f"Line1 has: {line1}")
        print(f"Line2 has: {line2}")
        line1.zigzag2(line2.getLine())
        print("Completed")
        print(f"Line1 has: {line1}")
        print(f"Line2 has: {line2}")

def teleport(x, y, t):
    t.ht()
    t.speed(0)
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()
    t.st()
    
def drawGraph(points,tur):
    teleport(-350,300,tur)
    tur.fd(20)
    tur.back(20)
    tur.right(90)
    for i in range(points):
        tur.fd(600/points)
        tur.left(90)
        tur.fd(20)
        tur.back(20)
        tur.right(90)
    tur.left(90)
    for i in range(points):
        tur.fd(600/points)
        tur.left(90)
        tur.fd(20)
        tur.back(20)
        tur.right(90)
        
    # tur.right(90)
    # tur.fd(600)
    # tur.left(90)
    # tur.fd(750)
    
def plot(tur):
    #Point(3,2)
    teleport(300,200,tur)
    tur.stamp()
    
def draw(tur):
    points = 5
    drawGraph(points,tur)
    teleport(-300,0,tur)
    tur.stamp()
    turtle.exitonclick()
    
#console()
tur = turtle.Turtle()
turtle.bgcolor("light blue")
draw(tur)