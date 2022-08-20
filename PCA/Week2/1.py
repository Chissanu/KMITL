def from_decimal(num, base):
    arr = []
    if base < 0:
        return "Error: Negative base"
    if base > 36:
        return "Error: Base > 36"
    if num == 0:
        return 0
    if num > 0:
        while num >= 1:
            arr.append(num % base)
            num = num / base
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        index = 0
        for i in arr:
            if i > 9:
                hexVal = i + 55
                arr[index] = chr(hexVal)
            index += 1
        arr.reverse()
        return ''.join(str(char) for char in arr)
    else:
        return "Error: Negative number"


def to_decimal(num, base):
    numSplit = []
    ans = 0
    if base < 0:
        return "Error: Negative base"
    elif base > 36:
        return "Error: Base over 36"
    if num.isalnum():
        pass
    elif int(num) < 0:
        return "Error: Negative number"
    for i in range(len(num)):
        numSplit.append(num[i])
        if numSplit[i].isalpha():
            temp = ord(numSplit[i])
            numSplit[i] = temp - 55
        elif int(numSplit[i]) < 0:
            return "Error: Negative number"
        elif int(numSplit[i]) > base:
            return "Error: Incorrect number/base"
    numSplit.reverse()
    for i in range(len(numSplit)):
        ans += int(numSplit[i]) * (base ** i)
    return ans

print(to_decimal('161609844',28))
