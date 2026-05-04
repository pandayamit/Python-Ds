class Employee:
    start_time="10am"
    end_time = "6pm"

class AdminStaff(Employee):
    def __init__(self,role):
        self.role=role

class Accountant(AdminStaff):
    def __init__(self,salary):
        self.salary=salary        