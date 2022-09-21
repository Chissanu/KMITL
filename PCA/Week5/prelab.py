def mystery(n):
    if len(n) == 1:
        return n[0]
    else:
        a = n.pop(0)
        b = mystery(n)
        if a > b:
            return a
        else:
            return b
        

myList = [1,2,3,4,5]
print(mystery(myList))