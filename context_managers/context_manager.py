text_file = """This is the contents of the text file.
This is the second row.
This is the texts on the third row.
The end."""


class Connection:
    def __init__(self, file):
        self.file = file 

    def __enter__(self):
        print(">> Connection opened")
        self.connection = 1
        return self # this is what will be returned after AS in context manager 

    def __exit__(self, exc_type, exc_val, traceback):
        self.connection = 0
        print(">> Connection closed")
        if exc_type:
            print(f">> Exception type: {exc_type} ")
            print(f">> Exception value: {exc_val} ")
            print(f">> Exception traceback: {traceback} ")



with Connection(text_file) as obj:
    print(f">> The contents of the file is:\n'{obj.file}'")
    # raise Exception("Something is wrong!")
