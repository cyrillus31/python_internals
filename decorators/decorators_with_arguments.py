# BELOW ARE THE DECORATORS THAT TAKE ARGUMENTS

def repeat(n):
 def decorator(func):
   def wrapper(*args, **kwargs):
     print("BEFORE")
     # result = []
     for _ in range(n):
       r = func(*args, **kwargs)
       # result.append(r)
     print("AFTER")
     # return result

   return wrapper
 return decorator



# first option 
def say_hi(name):
  print(f"Hi, my name is still {name}")

repeat(3)(say_hi)("Kirillus")



# second option
@repeat(3)
def say_hi(name):
  print(f"Hi, my name is still {name}")

say_hi("Cyrillus")
