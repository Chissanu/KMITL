class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def getList(self):
        current = self.head
        tempList = []
        while current != None:
            tempList.append(current.getData())
            current = current.getNext()
        tempList.reverse()
        return tempList

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def printNode(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

    def squish(self):
        current = self.head
        while current != None:
            next = current.getNext()
            if next is not None:
                if current.getData() == next.getData():
                    current.setData(next.getData())
                    current.setNext(next.getNext())
                else:
                    current = current.getNext()
            else:
                break
    
    def dble(self):
        current = self.head
        while current != None:
            next = current.getNext()
            if next != None:
                dupe = current
                dupe.setNext(next)
                current.setNext(dupe)
                current = current.getNext()

def main():
    myList = UnorderedList()
    #ex = [0, 0, 0, 0, 1, 1, 0, 0, 0, 3, 3, 3, 1, 1, 0]
    ex = [3,7,4,2]
    for i in ex:
        myList.add(i)

    # print("Before Squish:")
    # print(myList.getList())
    # myList.squish()
    # print("After Squish")
    # print(myList.getList())
    print("Before Double")
    print(myList.getList())
    myList.dble()
    print("After Double")
    print(myList.getList())
    

main()