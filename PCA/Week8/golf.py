class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev

    def setData(self,newData):
        self.data = newData

    def setNext(self,newNext):
        self.next = newNext
    
    def setPrev(self,newPrev):
        self.prev = newPrev
        
class UnorderedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        newNode = Node(item)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode
    
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


def main():
    myList = UnorderedList()
    myList.add("Oak")
    myList.add("John")
    myList.add("Ruj")
    myList.printNode()
    #print(myList.getList())
    
main()
    
    