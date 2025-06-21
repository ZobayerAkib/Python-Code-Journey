#This is Hierarchical Inheritance
class User:
   def reg(self):
       print("Registration is done")
   def login(self):
       print("Login is done")

class Student(User): #inheritance
    def enroll(self):
        print("Enrolled Program")
    def review(self):
        print("Review done")
class Instructor(User): #inheritance
    def create_course(self):
        print("Course is created")

student1=Student()
student1.reg()
student1.review()
student1.login()
print("<------------------------------------------>")
ins1=Instructor()
ins1.login()
ins1.create_course()
