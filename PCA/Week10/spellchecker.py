def hash(str):
    h = 0
    for ch in str:
        h *= 37
        h += ord(ch)
    return h

# def spellCheck(word):
#     wordHash = hash(word)
#     for i in hashDict.values():
#         if wordHash == i:
#             return True

def hashWords(words):
    pass
    
hashTable = []
f = open("PCA/Week10/small.txt", "r")
words = f.read().split()

# for word in words:
#     hashDict[word] = hash(word)

# userInput = input("Enter your word : ")
# correct = spellCheck(userInput)
# if correct == True:
#     print(f"{userInput} is correctly spelled")
# else:
#     print(f"{userInput} is not in the dictionary")
    
print(hash("aaa"))