class Account:
    bank='Equity'
    def __init__(self,accountNumber,accountName,branch):
        self.accountName=accountName
        self.accountNumber=accountNumber
        self.branch=branch
    def describe_account(self):
        return f"this {self.bank} of this account number {self.accountNumber} is owned by {self.accountName}"
    def withdraw_money():
        return
            
        