class Human:
    male_humans = []
    female_humans = []

    def __init__(self, name):
        self.name = name
        self._gender = None

    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, sex: str):
        if sex.lower() == "male":
            self._gender = "m"

        elif sex.lower() == "female":
            self._gender = "f"

        else:
            print(f"This '{sex}' gender cannot be assigned. Use 'male' or 'female'.")


kirill = Human("Kirill")
karine = Human("Karine")

kirill.gender = "masculine"
karine.gender = "woman"

kirill.gender = "male"
karine.gender = "female"

print(kirill.__dict__)
print(karine.__dict__)





