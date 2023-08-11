import classes
import main

transactions = []

transactions.append(transaction(1, 100, 'withdraw'))

def check_amt(amount, bank_id, action):
    if action == 'withdraw' or 'Transfer Funds':
        for i in range(len(bank_id)):
            if bank_id == bank_id[i].bank_id:
                if amount > bank_id[i].balance:
                    return True
        return False
    else:
        return True


def transact(amount, action, bank_id, target_bank_id):
    #validate here or in outer function
    if action ==  'withdraw':
        #withdraw
        for i in range(len(bank_list)):
            if user_input == bank_list[i].bank_id:
                print('Correct ID')
                valid = True
        account.balance -= amount
    elif action == 'deposit':
        #deposit
    else:
        #transfer