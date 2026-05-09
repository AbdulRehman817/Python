class BankAccount:
    total_accounts=0
    def __init__(self,owner_name,balance):
        self.__owner_name=owner_name
        self.__balance=balance
        BankAccount.total_accounts+=1
    def show_details(self):
        return f"Account Owner: {self.__owner_name} | Balance: {self.__balance}"
    
    def get_balance(self):
        return self.__balance;
    
    def deposit(self,new_balance):
        self.__balance+=new_balance
        
    def withdraw(self,amount):
        if amount>self.__balance:
            return "Insufficient money"
        self.__balance-=amount;
        
    def account_type(self):
        return "Standard Account"
    @staticmethod
    def bank_description():
        return "Welcome to ABC Bank — Safe and Secure"
    @property
    def owner_name(self):
        return self.__owner_name;
class SavingsAccount(BankAccount):
    def __init__(self,owner_name,balance,interest_rate):
        super().__init__(owner_name,balance)
        self.interest_rate=interest_rate
    def account_type(self):
        return "Savings Account"
class Rewards:
    def add_points(self,amount):
        print(f"Reward Points Added: {amount // 10}")
        
class RewardAccount(SavingsAccount,Rewards):
    def __init__(self, owner_name, balance, interest_rate):
        super().__init__(owner_name, balance, interest_rate)
    
    def deposit(self, amount):
        result= super().deposit(amount)
        self.add_points(amount)
    
my_bank=BankAccount("Abdul Rehman","200$")
my_bank.owner_name=="Ali"
# my_bank=BankAccount("Ali","300$")
# my_bank=BankAccount("Abdullah","500$")
# my_bank.deposit("500$")
# my_bank.withdraw("200$")
# print(my_bank.show_details())
# print(my_bank.get_balance())
# print(BankAccount.total_accounts)
# print(my_bank.bank_description())
print(my_bank.owner_name)
print(isinstance(my_bank,BankAccount))
print(isinstance(my_bank,SavingsAccount))