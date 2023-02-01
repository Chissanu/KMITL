num = int(input("Whats the number? >"))
val = 1
for i in range(num):
    val += val * i
    
print(val)