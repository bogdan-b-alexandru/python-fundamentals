class Student:

    def __init__(self, name, school) :
        self.name = name
        self.school = school
        self.courses = []
    

    def enroll(self, course):
        self.courses.append(course)
    

    def introduce(self):
        print(f"Hi, im {self.name}  from  {self.school}  enrolled in:  {self.course}")
    
bogdan = Student(" Bogdan ", " ETS ")
sarah = Student(" Sarah ", " Concordia ")

bogdan.enroll("Python")
bogdan.introduce()

sarah.enroll("Flask")
sarah.introduce()