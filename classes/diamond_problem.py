class A:
    def __str__(self):
        return "This is A"

class B(A):
    def __str__(self):
        return "This is B"

class C(A):
    def __str__(self):
        return "This is C"

class D(B, C):
    # def __str__(self):
    #     return "This is D"
    pass


print(D())
print("Python inherits in the following order here: D, B, C, A")
