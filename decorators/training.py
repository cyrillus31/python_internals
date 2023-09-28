def greet_politely(second_name):
    def decorator(func):
        def wrapper(*arg, **kwarg):
            name = arg[0]
            polite_name = name + " " + second_name
            func(polite_name)
        return wrapper
    return decorator

@greet_politely("Fedtsov")
def greet(name):
    print(f"Hello, {name}")

greet("Kirill")

# >> Hello, Kirill Fedtsov
