"""
Student Grade Calculator: Implement a Student class with attributes for name and a list of marks.
Include a method to calculate the average and determine the grade.
"""

class Grade:
    def __init__(self,name,numbers):
        self.name=name
        self.numbers=numbers

    def avg_marks(self):
        avg= sum(self.numbers)/len(self.numbers)
        return avg
    def grade_calculation(self):
        avg=self.avg_marks()
        if(avg>=80):
            print("The grade is A+")
        elif(avg>=70 and avg<80):
            print("The grade is A")
        else:
            print("The grade is B")

s1=Grade("Akib",[70,80,90])
print(f"The name of Student: {s1.name} ")
s1.grade_calculation()