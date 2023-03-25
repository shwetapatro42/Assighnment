#CHALLENGE 4
class Account:  #create class 
    def _init_(self,title=None,Balance=0):
        self.title=title
        self.Balance=Balance


class SavingsAccount(Account):  #create subclass
    def _init_(self,title,Balance,interestRate):
        self.interestRate=interestRate
        super()._init_(title,Balance)
        
    def display(self): 
      return(f" Account Holder Name : {self.title}  \n Account Balance : {self.Balance} Rs. Only \n Interest Rate : {self.interestRate} % ") 
print("Hello!!! Welcome to Central bank ")         
obj=SavingsAccount("Shweta",1000,5)
print(obj.display())