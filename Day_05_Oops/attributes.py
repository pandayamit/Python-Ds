class Student:
    college_name="Inidia college"   #class attribute

    def __init__(self,name,gpa):
        self.name=name    # instance attributes
        self.gpa=gpa

stu1=Student("Amit",7.39)
print(f"Name: {stu1.name}, gpa: {stu1.gpa} college: {stu1.college_name}")
print(f"{Student.college_name}")


'''
Note: 

'''