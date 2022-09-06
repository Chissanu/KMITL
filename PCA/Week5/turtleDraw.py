def test(n):
    if n == 1:
        return 1
    else:
        return test(n-1)
        test(n-1)
        
print(test(5))