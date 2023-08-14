from datetime import date

class customer:
    def __init__(self, bank_id, user_name, balance):
        self.bank_id = bank_id
        self.user_name = user_name
        self.balance = balance

class account:
    #account_type = 'Savings'
     def __init__(self, bank_id, user_name, balance):
        self.bank_id = bank_id
        self.user_name = user_name
        self.balance = balance
    

class transaction:
    def __init__(self, transaction_id, bank_id, target_id, amount, action, balance):
        self.transaction_id = transaction_id
        self.amount = amount
        self.action = action
        self.date = date.today()
        self.bank_id = bank_id
        self.target_id = target_id
        self.balance = balance