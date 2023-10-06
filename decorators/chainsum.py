def chainsum1(a=None, prev=[0]):
    if a is not None:
        prev[0] += a
        return chainsum1
    else:
        return prev[0]

def chainsum2(a):
    sum = a
    def wrapper(number=None):
        nonlocal sum
        if number is not None:
            sum = sum + number 
            return wrapper
        else:
            return sum 
    return wrapper

r1 = chainsum1(4)(5)(10)()
r2 = chainsum2(4)(5)(10)()
print(r1, r2)




