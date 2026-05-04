class BankAccount:
    def __init__(self,name,balance):
        self.name=name      #public
        # self._balance=balance     #protected
        self.__balance=balance     #private

    def get_info(self):
        # print(f"Your bank name is {self.name} & and have a balance of Rs. {self._balance} only")
        print(f"Your bank name is {self.name} & and have a balance of Rs. {self.__balance} only")

    def get_balance(self):   #getter
        return self.__balance

    def set_balance(self,newBalance):  #setter
         self.__balance=newBalance
    

b1=BankAccount("Bank of India", 400000)
b2=BankAccount("Punjab National Bank",1000000)


b1.get_info()
b2.get_info()

b1.set_balance(5000000)
print(b1.name,b1.get_balance())
# print(b1.name,b1._BankAccount__balance)  # Trick to get private route access outside the class 
# print(b2.name,b2._balance)  # Trick to get protected route access outside the class