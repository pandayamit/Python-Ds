'''
Design & create an online store for products (name,price)
track total products being created 
create a static method to calculate discount on each product based on a % parameter

'''

class Product:
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count +=1

    def get_info(self):
        print(f"Price of {self.name} is Rs. {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total product in store ={cls.count}")



    @staticmethod
    def calc_discount(price,percentage):
        final_price= price-(price*percentage/100)
        print(f"Discounted Price is: {final_price}")    


p1=Product("Laptop",30000)
p2=Product("Notebook",40)
p3=Product("Shoes",1200)


p1.get_info()
Product.get_count()

p1.calc_discount(30000,10)
Product.calc_discount(30000,10)


