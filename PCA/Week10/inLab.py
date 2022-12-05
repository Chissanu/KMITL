import os
import math

class node: # For linked list
    def __init__(self, data):
        self.next = None
        self.nodeData = data

class hashtable:
    def __init__(self, arr):
        self.hash_table = [] # Total number of spaces
        self.inputArr = arr # Array input from dictionary
        self.length = getNextPrime(round(len(arr) * 0.2)) # Get next prime number of 20% of length of array
        for i in range(self.length):
            self.hash_table.append(" ")   # add space string to represent space in an array
        self.expansion = 0
        self.load_factor = 0
        self.collisions = 0
        self.longest = 0

    def hash(self, str): # given hash function
        h = 0
        for ch in str:
            h *= 37
            h += ord(ch)
        return h

    def clear_table(self): # clear table
        for i in range(self.length):
            self.hash_table.pop()

    def convertToIndex(self, key): # mod and convert to index
        return key % self.length

    def separate(self): # separate chaining function
        chain_length = 1
        entry = round(0.5 * self.length) # Get the number of input to reach the 0.5 load factor
        rehash = False
        for i in range(len(self.inputArr)): # for every word in the dictionary
            wordNode = node(self.inputArr[i]) # make the word a node
            key = self.hash(self.inputArr[i]) # hash and get the key of the string
            index = self.convertToIndex(key) # convert to index
            if i >= entry: # check if total word is more than the 0.5 load factor
                self.expansion += 1
                rehash = True
                self.longest = 0
                break
            if self.hash_table[index] == " ": # check if the converted index is empty
                self.hash_table[index] = wordNode # make empty index a node
            else: # array is not empty
                try:
                    check = self.hash_table[index].next # check if there is any next node in the linked list
                    while check.next != None: # if there is then go to last node and add the current to last node
                        check = check.next
                        chain_length += 1
                    check.next = wordNode
                    if chain_length > self.longest: # if the counted chain is longer than the longest recorded then add it
                        self.longest = chain_length
                except:
                    self.hash_table[index].next = wordNode
            self.load_factor = i / len(self.hash_table) # calculate load factor
        if rehash:
            self.rehash(1)
            
    def rehash(self, mode): # rehash
        self.clear_table() # clear table
        self.length = getNextPrime(self.length * 2) # get next prime of 2x the length
        for i in range(self.length):
            self.hash_table.append(" ") # add spaces
        if mode == 1:
            self.separate()
        else:
            self.linear()

    def showTableSeparate(self): # show the separate table
        for i in self.hash_table:
            arr = []
            if type(i) != str: # check if i is space and not node
                while i != None:
                    arr.append(i.nodeData)
                    i = i.next
                print(arr)
            else:
                arr.append(i)
                print(arr)

    def find(self, str): # 
        key = self.hash(str)
        index = self.convertToIndex(key)
        current = self.hash_table[index]
        while current != None:
            if current.nodeData == " ":
                break
            if current == str:
                return (f'"{str}" is correctly spelled')
            else:
                current = current.next
        return (f'"{str}" is not in the dictionary')

    def linear(self):
        collisions = 0
        entry = round(0.5 * self.length)
        rehash = False
        for i in range(len(self.inputArr)):
            key = self.hash(self.inputArr[i])
            index = self.convertToIndex(key)
            if i >= entry:
                self.expansion += 1
                rehash = True
                self.collisions = 0
                break
            if self.hash_table[index] == " ":
                self.hash_table[index] = self.inputArr[i]
            else:
                j = 1
                while True:
                    index = self.convertToIndex(key + j)
                    if self.hash_table[index] == " ":
                        self.hash_table[index] = self.inputArr[i]
                        break
                    else:
                        j += 1
                if j > self.collisions:
                    self.collisions = j
            self.load_factor = i / len(self.hash_table) 
        if rehash:
            self.rehash(2)

    def showTableLinear(self):
        j = 0
        for i in self.hash_table:
            if i == " ":
                continue
            else:
                j += 1
        return self.hash_table

    def search(self, str):
        key = self.hash(str)
        index = self.convertToIndex(key)
        initialIndex = index
        found = False
        if self.hash_table[index] == str:
            found = True
        else:
            j = 1
            index = self.convertToIndex(key + j)
            while index != initialIndex:
                index = self.convertToIndex(key + j)
                if self.hash_table[index] == str:
                    found = True
                    break
                j += 1
        if found:
            return (f'"{str}" is correctly spelled')
        else:
            return (f'"{str}" is not in the dictionary')
                
def getNextPrime(num):
    prime = False
    while not prime:
        if '.' in str(math.sqrt(num)):
            for i in range(2, num - 1):
                if num % i != 0:
                    prime = True
                    continue
                else:
                    num += 1
                    prime = False
                    break
        else:
            num += 1
    return num

def start():
    userInput = input("Enter a word to search: ")
    hash_table = hashtable(data)
    userMode = int(input("1. Separate Chaining, 2. Linear Probing: "))
    if userMode == 1:
        hash_table.separate()
        #hash_table.showTableSeparate()
        print(hash_table.find(userInput))
        #print(f"Total Words: len(data)")
        print(f"Collision resolution : Separate Chaining")
        print(f"{hash_table.expansion} expansions")
        print(f"load factor {hash_table.load_factor}")
        print(f"longest chain {hash_table.longest}")
    else:
        hash_table.linear()
        #print(hash_table.showTableLinear())
        print(hash_table.search(userInput))
        print(f"Collision resolution : Linear Probing")
        print(f"{hash_table.expansion} expansions")
        print(f"load factor {hash_table.load_factor}")
        print(f"{hash_table.collisions} collisions")

file = open("PCA\Week10\small.txt", "r")
data = file.read()
file.close()
data = data.split(" ")

start()