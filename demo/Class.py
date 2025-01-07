class Account:
        """一个余额非零的账户。"""
        interest = 0.02
        def __init__(self, account_holder):
            self.balance = 0
            self.holder = account_holder
        def deposit(self, amount):
            """存入账户 amount, 并返回变化后的余额"""
            self.balance = self.balance + amount
            return self.balance
        def withdraw(self, amount):
            """从账号中取出 amount, 并返回变化后的余额"""
            if amount > self.balance:
                return 'Insufficient funds'
            self.balance = self.balance - amount
            return self.balance
        
class CheckingAccount(Account):
    """从账号取钱会扣出手续费的账号"""
    withdraw_charge = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)
    
checking = CheckingAccount('Sam')
print(checking.deposit(10))
print(checking.withdraw(5))
print(checking.interest)