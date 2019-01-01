class Base(object):
    x=20
    # Constructor
    def __init__(self, x):
        self.x=x 

class Derived(Base):

    # Constructor
    def __init__(self, x, y):
#         print(super().x)
        #super(Derived,self).__init__(40)
        super().__init__(40)
        
obj=Derived(1,2)
print(obj.x)
print(Base.x)
