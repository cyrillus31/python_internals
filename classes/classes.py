class Person:
    species = "mammal"
    
    @classmethod
    def feed(cls):
        print("I ate")

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


Person.feed()
kirill = Person("Kirill", "male")
print(type(kirill.feed()), "oh no")

