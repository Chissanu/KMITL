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
    #Gen points Line2
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
        
    
def plot(tur,points,maxPoint,color):
    line = 600 / maxPoint
    teleport(-350 + points[0][0],-300 + points[0][1],tur)
    for i in range(len(points)):
        pointX = points[i][0] * line
        pointY = points[i][1] * line
        # if points[i][0] < 0:
        #     pointX = pointX * -1
        # if points[i][1] < 0:
        #     pointY = pointY * -1
        tur.goto(-350 + pointX,-300 + pointY)
        tur.dot(10,color)
    
def draw(tur):
    points = []
    line1 = int(input("How many points for line1? >"))
    #Gen points Line1
    for i in range(line1):
        randx = random.randint(0,line1)
        randy = random.randint(0,line1)
        point = (randx,randy)
        points.append(point)
    line1 = Line(points)

    points = []
    line2 = int(input("How many points for line2? >"))
    #Gen points Line2
    for i in range(line2):
        randx = random.randint(0,line2)
        randy = random.randint(0,line2)
        point = (randx,randy)
        points.append(point)
    line2 = Line(points)
    
    
    #Test
    print(f"Line1 has: {line1.getLine()}")
    print(f"Line2 has: {line2.getLine()}")
    
    #Draw graph
    if len(line1.getLine()) > len(line2.getLine()):
        maxPoint = len(line1.getLine())
    else:
        maxPoint = len(line2.getLine())
    drawGraph(maxPoint,tur)
    tur.speed(2)
    plot(tur,line1.getLine(),maxPoint,"red")
    plot(tur,line2.getLine(),maxPoint,"blue")
    
    #Ask for choice
    print("What do you want to do")
    print("\t1.Join")
    print("\t2.Join Zigzag1")
    print("\t3.Join Zigzag2")
    option = int(input("What do you want to do >"))
    if option == 1:
        err = line1.joinExtend(line2.getLine())
        tur.clear()
        drawGraph(maxPoint,tur)
        plot(tur,line1.getLine(),maxPoint,"red")
        if err == True:
            line2 = []
        print(line1.getLine())
        print(line2)
    elif option == 2:
        tur.clear()
        line3 = line1.zigzag1(line2.getLine())
        drawGraph(maxPoint,tur)
        print(line3)
        plot(tur,line3,maxPoint,"green")
    elif option == 3:
        tur.clear()
        drawGraph(maxPoint,tur)
        line1.zigzag2(line2.getLine())
        plot(tur,line1.getLine(),maxPoint,"red")
        
        
        
    # drawGraph(maxPoint,tur)
    # tur.speed(2)
    # plot(tur,line1,maxPoint,"red")
    # plot(tur,line2,maxPoint,"blue")
    turtle.exitonclick()
    
#console()
tur = turtle.Turtle()
tur.width(2)
tur.ht()
turtle.bgcolor("light blue")
draw(tur)