class niranjan:
  x = 5
  species = "human"
#__init__ function is called every time the class is being used
# self is the reference parameter for that class it can be name any other
  def __init__(self,name,age):
   self.name = name
   self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
  def sing(self, song):
  #format function in function instances of class
        return "{} sings {}".format(self.name, song)
    
 
nonu = niranjan("nonu",10)
print(nonu.x)
print(nonu.name)
print(nonu.age)
nonu.myfunc()
#modifying object properties
nonu.age = 40
print(nonu.age)
#format function
print("nonu is a {}".format(nonu.__class__.species))
print("{} is {} years old".format( nonu.name, nonu.age))
#del nonu - will delete complete object also used as del nonu.age

"""
to amde any empy class use pass keyword as
class niranjan:
 pass
"""
print(nonu.sing("'Happy'"))

