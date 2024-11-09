import pandas as pd
class BookLover:
    '''
        This class creates an object with the following attributes: name, email, fav_genre, num_books, and book_list.
        The name, email and fav_genre attributes are required when initializing the object while the num_books and book_list variables are optional. 
        
        It has the following methods:
            add_book - allows us to insert a book and a rating
            has_read - checks if the book exists in the list
            num_books_read - returns the number of books read
            fav_books - returns a df of books witha rating over 3
        '''
    # constructor
    def __init__(self, name, email, fav_genre, num_books=0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    # add book
    def add_book(self, book_name, rating): 
        if book_name not in self.book_list['book_name'].values:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
            })

            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        
        else:
            #raise Exception("Book already exists in list")
            print("Book already exists in list")
    
    #check if book exists in list
    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
    
    #return number of books read
    def num_books_read(self):
        return len(self.book_list)
    
    #return list of favorite books - with ratings greater than 3
    def fav_books(self):
        self.filtered_books = self.book_list[self.book_list['book_rating'] > 3]
        return self.filtered_books

