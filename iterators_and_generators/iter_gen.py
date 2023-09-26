class BookshelfAuthorsIterator:
    def __init__(self, bookshelf):
        self.books = bookshelf.books
        self.cur_b_num = 0
        self.cur_a_num = 0

    def __next__(self):
        if len(self.books) == 0:
            raise StopIteration

        if self.cur_a_num > len(self.books[self.cur_b_num]["authors"]) - 1:
            self.cur_b_num += 1
            self.cur_a_num = 0

        if self.cur_b_num > len(self.books) - 1:
            raise StopIteration

        current_author = self.books[self.cur_b_num]["authors"][self.cur_a_num] 
        self.cur_a_num += 1 
        return current_author




class Bookshelf:
    def __init__(self):
        self.books = []

    def add_book(self, book: dict):
        if isinstance(book, dict):
            if ("authors" not in book) and ("title" not in book):
                raise ValueError("The book must have keys 'authors' and 'title'")
        else:
            raise ValueError("The book must be of type dict")
        self.books.append(book)

    def __iter__(self):
        return BookshelfAuthorsIterator(self)


mybookshelf = Bookshelf()
book0 = {"authors": [], "title": "Short stories"}
book1 = {"authors": ["Hemingway", "Salinger", "King"], "title": "Short stories"}
book2 = {"authors": ["Dostoyevsky"], "title": "Demons"}
mybookshelf.add_book(book0)
mybookshelf.add_book(book1)
mybookshelf.add_book(book2)

for author in mybookshelf:
    print(author)
