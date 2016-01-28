#Write MyBook class

from abc import ABCMeta, abstractmethod
class Book:
    __metaclass__ = ABCMeta
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

class MyBook(Book):
    def __init__(self, title, author, price):
        # Book.__init__(self, title, author)
        self.title=title
        self.author=author
        self.price = price
    def display(self):
    	print "Title:", self.title
    	print "Author:", self.author
    	print "Price:", self.price

mb = MyBook("as","boula", 122)
mb.display()