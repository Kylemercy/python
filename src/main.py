

class Article:
    def __init__(self, title, page_count):
        # initialize protected attributes
        self._title = title
        self._page_count = page_count
         
    # define protected method
    def _show(self):
        # access protected attributes inside class 
        print("Article Title: ", self._title)
        print("Page Count: ", self._page_count)
         
class Author(Article):
    def __init__(self, name, title, page_count):
        Article.__init__(self, title, page_count)
        self.name = name
    def display(self):
        print("Author Name: ", self.name)
        # access Article's protected method
        self._show()
        print("------------------ \n")
         
         
author = Author("Eyong Kevin", "Python Classes and Objects", 3000)
author.display()
# access protected data
print(author._title) 







class Article:
  def __init__(self, title,pages):
    self._title = title
    self._pages = pages
  
  
  def _show(self):
    #_is use to make a protected method
    print("The Article title is ",self._title,".")
    print("The number of pages is ",self._pages,".")
    
    
class Author(Article):
  def __init__(self,name,title,pages):
    Article.__init__(self, title,pages)
    self.name = name
  
  
  def display(self):
    print("Author name: ",self.name)
    self._show()
    print("----------------------\n")

author = Author("adele","songs of echo",46)
author.display()
print(author._title)
  
  

  




