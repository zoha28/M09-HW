import unittest
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        book = "War of the Worlds"
        test_object.has_read("War of the Worlds")
        self.assertTrue(book in test_object.book_list['book_name'].values)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("John Smith", "john.smith@gmail.com", "mystery")
        test_object.add_book("Silent Patient", 5)
        test_object.add_book("Silent Patient", 5)
        expected = 1
        #self.assertEqual(test_object.num_books, expected)
        self.assertEqual(test_object.book_list['book_name'].value_counts()["Silent Patient"], expected)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object = BookLover("John Smith", "john.smith@gmail.com", "mystery")
        test_object.add_book("Silent Patient", 5)
        #print(test_object.has_read("Silent Patient"))
        self.assertTrue(test_object.has_read("Silent Patient"))

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object = BookLover("John Smith", "john.smith@gmail.com", "mystery")
        self.assertFalse(test_object.has_read("Mystery book"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_object = BookLover("John Smith", "john.smith@gmail.com", "mystery")
        test_object.add_book("Jane Eyre", 4)
        test_object.add_book("Fight Club", 3)
        test_object.add_book("The Divine Comedy", 5)
        test_object.add_book("The Popol Vuh", 5)
        expected = 4
        self.assertEqual(test_object.num_books_read(), expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_object = BookLover("John Smith", "john.smith@gmail.com", "mystery")
        test_object.add_book("Jane Eyre", 4)
        test_object.add_book("Fight Club", 3)
        test_object.add_book("The Divine Comedy", 5)
        favbooks = test_object.fav_books()
        for i in favbooks['book_rating']:
            if (i <= 3):
                print("Rating isn't greater than 3")
                pass_test = False
            else:
                pass_test = True
        self.assertTrue(pass_test, True)
                   
            
if __name__ == '__main__':
    
    unittest.main(verbosity=3)