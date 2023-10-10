from abc import ABC,abstractmethod

class bankingapp(ABC):

    @abstractmethod
    def transfer(self):
        pass

    @abstractmethod
    def balance_check(self):
        pass

    @abstractmethod
    def transaction_details(self):
        pass

class phonepay(bankingapp):

    
   
    def transfer(self):
        print("transfer")
        

    
    def balance_check(self):
         print("balance_check")

    
    def transaction_details(self):
        print("transaction_details")

obj=phonepay()
obj.transfer()
obj.balance_check()
obj.transaction_details()