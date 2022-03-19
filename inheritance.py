class niranjan:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)

#extended/derived inherited child class from base/parent class
class Student(niranjan):
  def __init__(self, fname, lname, year):
    #niranjan.__init__(self, fname, lname)
    #also super() func can be used
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Niranjan", "Kalra", 2001)
x.printname()
x.welcome()
