import random
import os

class stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)

    def pop(self):
        popElement = self.stack[-1]
        self.stack.pop(-1)
        return popElement

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
            
    def size(self):
        return len(self.stack)

    def contain(self, element):
        if element in self.stack:
            return True
        else:
            return False

    def returnLs(self):
        return self.stack

class Parking():
    def __init__(self):
        self.parkingLane = stack()

    def getLanes(self):
        return self.parkingLane.returnLs()
    
    def park(self,carName):
        self.parkingLane.push(carName)
    
    def backOut(self,carName,lanes):
        if self.parkingLane.contain(carName):
            carList = []
            while not self.parkingLane.is_empty():
                removedCar = self.parkingLane.peek()
                # removedCar = self.parkingLane.pop()
                if removedCar != carName:
                    removedCar = self.parkingLane.pop()
                    print(f"Moving {removedCar} to other lane")
                    lanes.park(removedCar)
                    print(self.parkingLane.returnLs())
                    print(lanes.getLanes())
                    print()
                    carList.append(removedCar)
                else:
                    self.parkingLane.pop()
                    if self.parkingLane.size() == 0:
                        return True
                    carList.reverse()
                    for car in carList:
                        self.parkingLane.push(car)
                        lanes.getLanes().remove(car)
                    return True


def gen():
    laneList = []
    #Gen lanes
    for i in range(2):
        laneList.append(Parking())
    #Gen random cars
    for lane in laneList:
        for i in range(random.randint(2,6)):
            lane.park(random.randint(0,1000))
    return laneList

def printLane():
    count = 1
    for lane in lanes:
        print(f"Lane:{count}",end="")
        print(lane.getLanes())
        count += 1

def main(lanes):
    option = int(input("1.Park 2.Backout :>"))
    if option == 1:
        #Ask for car plate
        carName = int(input("What's the car plate :>"))
        #Print lanes
        printLane()
        #Ask for plate inputs
        carLane = int(input("What lane do you want to park in? (1-2) >"))
        if carLane == 1:
            lanes[0].park(carName)
        else:
            lanes[1].park(carName)
        printLane()
    elif option == 2:
        printLane()
        carName = int(input("What's the car plate :>"))
        laneID = 1
        for lane in lanes:
            if carName in lane.getLanes():
                success = lane.backOut(carName,lanes[laneID])
                break
            else:
                laneID -= 1
                success = False
        if success == True:
            print("Finish taking out the car")
            printLane()
        else:
            print("No matched car")


lanes = gen()
main(lanes)
