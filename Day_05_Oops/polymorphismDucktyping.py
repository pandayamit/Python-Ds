class Teacher:
    def get_designation(self):
        print("Designation = Teacher")

class  Accountant():
    def get_designation(self):
        print("Designation = Accountant")



t1=Teacher()
t2=Accountant()
t1.get_designation()
t2.get_designation()