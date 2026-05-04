class Laptop:
    storage_type="ssd"

    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage= storage

    def get_info(self):   # Instance Methods
        print(f"Laptop has {self.RAM} RAM, {self.storage} & storage type is {self.storage_type}")
        print("--------------------Instance Method ----------------------") 
    
    @classmethod
    def get_storage_type(cls):
        print(f"storage type is: {cls.storage_type}")
        print("---------------class Method-----------------") 


    @staticmethod
    def calc_discount(price,discount):
        final_price=price-(discount*price/100)
        print(f"Discounted price of laptop is: {final_price}")         

l1=Laptop("16gb","512gb")
l2= Laptop("8gb","256gb")

l1.get_info()
l1.get_storage_type()
Laptop.get_storage_type()
l1.calc_discount(10000,10)
Laptop.calc_discount(20000,10)