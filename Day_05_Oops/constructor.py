class Student:
    def __init__(self):
        print("Constructor was called successfully")


stu1= Student()


#Eaxmple:2

class Car:
    def __init__(self,name,rank):
        self.name=name
        self.rank=rank
car1= Car("Nano",3)
car2=Car("Safari",1)
car3=Car("Hyuandai",2)
print(f"Car {car1.name} has rank {car1.rank}")
print(f"Car {car2.name} has rank {car2.rank}")      
print(f"Car {car3.name} has rank {car3.rank}")    

# ---------------------------------------------------------------------------------------------------

        #               Instance Methods 

class Toy:
    def __init__(self,name,rank,revenue):
        self.name=name
        self.rank=rank
        self.revenue=revenue
    def get_revenue(self):
          return self.revenue    

toy1= Toy("SpiderMan",2,500000)
toy2=Toy("IronMan",3,1000000)
toy3=Toy("Hulk",1,200000000)
print(f"Toy {toy1.name} has rank {toy1.rank} and revenue {toy1.get_revenue()}")
print(f"Toy {toy2.name} has rank {toy2.rank} and revenue {toy2.get_revenue()}")      
print(f"Toy {toy3.name} has rank {toy3.rank} and revenue {toy3.get_revenue()}")