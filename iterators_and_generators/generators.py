import sys

mylist = list(range(100))

def my_generator():
  for i in mylist:
    print(">> Here comes the number... ", end="")
    yield i

generator_object  = my_generator()    # the function is not executed here but a generator object is returned

for i in generator_object:
    print(i)

print(f">> The size of the list to be iterated over is {sys.getsizeof(mylist)}")
print(f">> The size of the generator object being used to generate all those elements of the mentioned list on the fly is {sys.getsizeof(generator_object)}")

def generator():
  yield 1
  yield 2
  yield "goodbye"

generator_object = generator()

for i in generator_object:
  print(i)
