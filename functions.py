import classes

def transact(amount, action, bank_id, target_bank_id):
    #validate here or in outer function
    if action ==  'withdraw':
        #withdraw
        for i in range(len(bank_list)):
            if bank_id == bank_list[i].bank_id:
                print('before:')
                print(bank_list[i].balance)
                bank_list[i].balance -= amount
                print('after')
                print(bank_list[i].balance)
    elif action == 'deposit':
        #deposit
        print('deposit')
    else:
        #transfer
        print('deposit')