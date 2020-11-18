class CurrentAccount:
    def __init__(self,customer_name):
        self.name=customer_name
    def get_customername(self):
        return self.name
account_holder=CurrentAccount("Rita Jones")
print("the customer name is", account_holder.get_customername())



class MayaNatural:
    def __init__(self,flax_oil_price,sesame_oil_price,flax_order_qty,sesame_order_qty):
        self.flaxoilprice=flax_oil_price
        self.sesameoilprice=sesame_oil_price
        self.flax_qty=flax_order_qty
        self.sesame_qty=sesame_order_qty
        self.ordervalue=0

    def get_ordervalue(self):
        flax_oil_ordervalue=self.flaxoilprice*self.flax_qty
        sesame_oil_ordervalue=self.sesameoilprice*self.sesame_qty
        ordervalue=flax_oil_ordervalue+sesame_oil_ordervalue
        self.ordervalue=self.ordervalue+ordervalue
        return self.ordervalue
    
    # def get_ordervalue(self):
    #     return self.ordervalue

total_order_value=MayaNatural(60,45,10,9)
print("The total ordervalue is", total_order_value.get_ordervalue())



class MayaNatural:
    def __init__(self,flax_oil_price,sesame_oil_price,flax_order_qty,sesame_order_qty):
        self.flaxoilprice=flax_oil_price
        self.sesameoilprice=sesame_oil_price
        self.flax_qty=flax_order_qty
        self.sesame_qty=sesame_order_qty
        self.ordervalue=0

    def ordervalue1(self):
        flax_oil_ordervalue=self.flaxoilprice*self.flax_qty
        sesame_oil_ordervalue=self.sesameoilprice*self.sesame_qty
        self.ordervalue=flax_oil_ordervalue+sesame_oil_ordervalue

        # self.ordervalue=self.ordervalue+ordervalue
        # return self.ordervalue
    
    def get_ordervalue(self):
        return self.ordervalue

total_order_value=MayaNatural(60,45,10,9)
total_order_value.ordervalue1()##messaging to change value of 

print("The total ordervalue is", total_order_value.get_ordervalue())

class MayaNatural:
    def __init__(self,flax_oil_price,sesame_oil_price,flax_order_qty,sesame_order_qty,ordervalue):
        self.flaxoilprice=flax_oil_price
        self.sesameoilprice=sesame_oil_price
        self.flax_qty=flax_order_qty
        self.sesame_qty=sesame_order_qty
        self.ordervalue=ordervalue

    def ordervalue1(self):
        flax_oil_ordervalue=self.flaxoilprice*self.flax_qty
        sesame_oil_ordervalue=self.sesameoilprice*self.sesame_qty
        self.ordervalue=flax_oil_ordervalue+sesame_oil_ordervalue

        # self.ordervalue=self.ordervalue+ordervalue
        # return self.ordervalue
    
    def get_ordervalue(self):
        return self.ordervalue

total_order_value=MayaNatural(60,45,10,9,0)
total_order_value.ordervalue1()##messaging to change value of 

print("The total ordervalue is", total_order_value.get_ordervalue())


import random
class Die:
    def __init__(self):
        self.side=0
    def throw(self):
        self.side=random.randint(1,6)
    def get_value(self):
        return self.side
my_die=Die()
my_die.throw()## Messaging to the object activating throw behaviour 
die_value=my_die.get_value()## messaging to getting value of the dice thrown
print("the value thrown is:", die_value)


import random
class Die:
    def __init__(self):
        self.side=0
    def throw(self):
        self.side=random.randint(1,6)
    def get_value(self):
        return self.side
my_die=Die()
for i in range (1,10):

    my_die.throw()## Messaging to the object activating throw behaviour 
    die_value=my_die.get_value()## messaging to getting value of the dice thrown
    print("the value thrown is:", die_value)

class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def credit(self,deposit):
        self.balance=self.balance+deposit
    
    def debit(self, withdrawal):
        self.balance=self.balance-withdrawal

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name  

    def set_name(self,name):
        self.name=name

customer=Account("Prakash",900)
print(customer.get_name(),"has got a balance of" , customer.get_balance())
customer.debit(90)
print(customer.get_name(),"has got a balance of", customer.get_balance())
customer.credit(90)
print(customer.get_name(),"has got a balance of", customer.get_balance())
customer.set_name("Maya")
print(customer.get_name(),"has got a balance of", customer.get_balance())


class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def credit(self,deposit):
        self.balance=self.balance+deposit
    
    def debit(self, withdrawal):
        self.balance=self.balance-withdrawal

    # def get_balance(self):
    #     return self.balance

    # def get_name(self):
    #     return self.name  

    # def set_name(self,name):
    #     self.name=name

customer=Account("Prakash",900)
print(customer.name,"has got a balance of" , customer.balance)
customer.debit(90)
print(customer.name,"has got a balance of", customer.balance)
customer.credit(90)
print(customer.name,"has got a balance of", customer.balance)
customer.name="Maya"
print(customer.name,"has got a balance of", customer.balance)


