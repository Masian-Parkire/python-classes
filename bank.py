class Account:
    bank='Equity'
    def __init__(self,accountNumber,accountName,branch):
        self.accountName=accountName
        self.accountNumber=accountNumber
        self.branch=branch
    def describe_account(self):
        return f"this {self.bank} of this account number {self.accountNumber} is owned by {self.accountName}"
    def withdraw_money(self):
        return f"I want to withdraw 5000 from account {self.accountNumber} of {self.accountName}"
    def send_money(self):
        return f" send money from {self.bank}{self.branch} to account number {self.accountNumber}"
            
        