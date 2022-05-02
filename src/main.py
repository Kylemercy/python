class Parent():
    def __init__(self, hair_color, temper):
        self.hair_color = hair_color
        self.temper = temper
    def sleeping_style(self):
        print('big fan of nap.')
  
class Child(Parent):
    def __init__(self, hair_color, temper):
        # call the base class init function
        #Parent.__init__(self,hair_color, temper )
        #or using super method
        super().__init__(hair_color, temper )
    def sleeping_style(self):
        # extending the base class method
        super().sleeping_style()
        print('tossing and turning.')
  
 
if __name__ == '__main__':
  
#this prevent code that is being imported from running

    # create instance of the child class
    enow = Parent ('black.', 'slow in anger.')
    enow.sleeping_style()
    print(enow.hair_color)
    print(enow.temper)
    print("***********************************\n")
    
    enow = Child('black.', 'slow in anger.')
    enow.sleeping_style()
    print(enow.hair_color)
    print(enow.temper)