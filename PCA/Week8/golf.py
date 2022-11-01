class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, new_val):
        new_node = Node(new_val)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert(self, previous_node, new_data):
        if previous_node is None:
            return
        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node
        new_node.prev = previous_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last
        return

    def listprint(self, node):
        print("The score board: ")
        while node is not None:
            print(node.data)
            last = node
            node = node.next

    def sortscore(self, item = []):
        current = self.head
        if current == None or item[1] < self.head.data[1]:
            self.push(item)
            return
        else:
            currentdata = current.data[1]
            while current != None:
                if item[1] >= currentdata:
                    current = current.next
                    if current == None:
                        self.append(item)
                        return
                    else:
                        currentdata = current.data[1]
                else:
                    self.insert(current.prev, item)
                    return

    def remove(self, name):
        current = self.head
        if current.data[0] == name:
            self.head = current.next
            return
        current = self.head
        while current != None:
            if current.data[0] == name:
                current.prev.next = current.next
                return
            else:
                current = current.next

    def update(self, name, score):
        current = self.head
        while current != None:
            current_name = current.data[0]
            if current_name == name:
                current.data[1] = score
                self.remove(name)
                if current.prev == None:
                    self.head = current.next
                    operator = [name, current.data[1]]
                    self.sortscore(operator)
                else:
                    current.prev.next = current.next
                    operator = [name, current.data[1]]
                    self.sortscore(operator)
                return
            current = current.next

    def retrieve(self, name):
        current = self.head
        while current != None:
            current_name = current.data[0]
            if name == current_name:
                print("Same Score:", name)
                currentscore = current.data[1]
                print(current.data)
                next = current.next
                prev = current.prev
                while prev != None and prev.data[1] == currentscore:
                    print(prev.data)
                    prev = prev.prev
                while next != None and next.data[1] == currentscore:
                    print(next.data)
                    next = next.next
                return
            current = current.next
        
    
myList = DoubleLinkedList()
myList.sortscore(["Jayden", 13])
myList.sortscore(["Jean", 13])
myList.sortscore(["Tom", 21])
myList.sortscore(["Rody", 18])
myList.sortscore(["Albert", 15])
myList.listprint(myList.head)
myList.retrieve("Jayden")
myList.remove("Jayden")
myList.listprint(myList.head)
myList.update("Jean", 5)
myList.listprint(myList.head)

    
    