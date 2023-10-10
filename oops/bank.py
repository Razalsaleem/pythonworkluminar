class bank:

    bank_name:str
    acno:str
    person_name:str
    ac_type:str
    balance:int

    def create(self,b_name,acno,p_name,ac_type,bal):
        self.bank_name=b_name
        self.acno=acno
        self.person_name=p_name
        self.ac_type=ac_type
        self.balance=bal


    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} has been created with {amount} avl balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("transaction failed insuficient balance ")
        else:
            self.balance-=amount
            print(f"your {self.bank_name} has been debited with {amount} avl balance is {self.balance}")

    def get_balance(self):
        print(f"your availabe balance={self.balance}")

obj1=bank()
obj1.create("sbi","10234","razal","savings",4000)

obj1.deposit(2000)

obj2=bank()
obj2.create("sbi","10236","ann","savings",5000)

