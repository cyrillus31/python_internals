def first_gen():
    yield "one"
    yield "two"

def second_gen():
    yield from first_gen() # Yield from another generator object
    yield 3 
    yield 4

gen_object = second_gen()
    
for element in gen_object:
    print(element)

