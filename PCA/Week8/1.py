class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def deleteNode(self,newNext):
        self.data = self.next
        self.next = newNext

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
    
    def deleteNode(self):
        current = self.head
        next = current.getNext()
        current.deleteNode(next)

    def printNode(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

    def squish(self):
        current = self.head
        while current != None:
            next = current.getNext()
            print(f"Comparing {current.getData()} and {next.getData()}")
            if next is not None:
                if current.getData() == next.getData():
                    current = current.getNext()
                    current.setNext(current.getNext())
                else:
                    current = current.getNext()
            else:
                break

        # while current != None:
        #     next = current.getNext()
        #     if next != None:
        #         if current.getData() == current.getNext().getData():
        #             self.remove(current.getData())
        #             current = current.getNext()
        #         else:
        #             current = current.getNext()
        #     else:
        #         current = current.getNext()
            # if current.getData() == current.getNext():
            #     self.remove(current.getData())
            #     current = current.getNext()
            # else:
            #     current = current.getNext()

def main():
    myList = UnorderedList()
    ex = [8, 0, 0, 0, 1, 1, 0, 0, 0, 3, 3, 3, 1, 1, 0]
    for i in ex:
        myList.add(i)

    print(myList.getList())
    print("Deleting")
    myList.deleteNode()
    print(myList.printNode())
    # print("Before Squish:")
    # print(myList.getList())
    # myList.squish()
    # print("After Squish")
    # print(myList.getList())

main()