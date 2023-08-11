from classes import account, customer
from functions import transact, check_amt


#customer_list = []
bank_list = []
transactions = []

bank_list.append(customer(1, 'Mayuri', 100))
bank_list.append(customer(2, 'Mig', 100))

# transactions.append(transactions(1, 100, 'withdraw'))

#print(bank_list)

# Check validity of Bank ID
def check_validity(user_input):
    for i in range(len(bank_list)):
        if user_input == bank_list[i].bank_id:
            print('Correct ID')
            valid = True
            return valid
    return False

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
        for i in range(len(bank_list)):
            if bank_id == bank_list[i].bank_id:
                print('before:')
                print(bank_list[i].balance)
                bank_list[i].balance += amount
                print('after')
                print(bank_list[i].balance)
    elif action == 'transfer':
        #transfer
        for i in range(len(bank_list)):
            if bank_id == bank_list[i].bank_id:
                for i in range(len(bank_list)):
                    print('before:')
                    print(bank_list[i].balance)
                    bank_list[i].balance += amount
                    print('after')
                    print(bank_list[i].balance)
    else:
        print('Invalid input')

valid = False 
while valid == False:
    user_input = int(input('Please input your bank id : '))
    valid = check_validity(user_input)
    if valid: 
        action_input = input('What would you like to do - See Transactions / Withdraw / Deposit / Transfer Funds : ')   
        if (action_input != 'See Transactions' and action_input != 'Transfer Funds'):
            amount = int(input(f'Please enter the amount you want to {action_input} : '))
            # Check if there is sufficient amount
            if check_amt(amount, user_input, action_input):
                print('You can continue')
            else:
                print('You have insufficient Fund')
                #transact(amount, action_input, user_input, '')
                # Check if i can withdraw that amount
                # Action of withdrawing
        else:
            print('False')
    else: 
    # If Bank ID is incorrect
    #if valid == False:
        print('Invalid ID, please try again later!')
