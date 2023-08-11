
transactions = []

transactions.append(transaction(1, 100, 'withdraw'))
class transaction:

    def  __init__(self, amount, action):
        
    def __init__(self, bank_id, target_bank_id, amount, action, balance):
        self.bank_id = bank_id
        self.target_bank_id = target_bank_id
        self.amount = amount
        self.action = action
        self.balance = balance
        self.transaction_id = int(max(list(transactions.transaction_id))) + 1
        #validate amount input
        if amount =< 0:
            return False
        if action == 'withdraw':
            if self.amount > self.balance:
                print("Insufficient funds")
                return False
            else:
                #transfer process
                self.balance -= self.amount


