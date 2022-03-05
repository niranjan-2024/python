class parrot:
   species = "bird"
   def __init__(self,name,age):
      self.name = name
      self.age = age
      
   def sing(self, song):
        return "{} sings {}".format(self.name, song)

   def dance(self):
        return "{} is now dancing".format(self.name)
        
peacock = parrot("peacock",10)   
pigeon = parrot("pigeon",15)
   
print("peacock is a {}".format(peacock.__class__.species))
print("pigeon is also a {}".format(pigeon.__class__.species))

print("{} is {} years old".format( peacock.name, peacock.age))
print("{} is {} years old".format( pigeon.name, pigeon.age))

print(peacock.sing("'Happy'"))
print(pigeon.dance())
