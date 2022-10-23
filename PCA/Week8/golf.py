class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
            self.head = newNode
    
    def insertAt(self,prevNode,data):
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        if newNode.next is not None:
            newNode.next.prev = newNode
        
    
    


def main():
    myList = DoubleLinkedList()
    myList.push("Oak")
    myList.push("Ruj")
    myList.push("4th")
    myList.push("Ton")
    #print(myList.getList())
    
main()
    
    