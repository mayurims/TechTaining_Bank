from classes import account, customer
import random

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
            #print('Correct ID')
            valid = True
            return valid
    return False

def check_amt(amount, bank_id, action):
    if action == 'withdraw' or action == 'transfer':
        for i in range(len(bank_list)):
            if bank_id == bank_list[i].bank_id:
                if amount < bank_list[i].balance:
                    return True
        return False
    else:
        return True

def transid_gen():
    num = 0
    while num in list(transactions.transaction_id):
        num = random.randint(0,999999)
    return num


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
                transactions.append(transaction(transid_gen(), amount, 'withdraw'))

        #transactions.append
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
                for j in range(len(bank_list)):
                    if target_bank_id == bank_list[j].bank_id:
                        print('sender before:')
                        print(bank_list[i].balance)
                        bank_list[i].balance -= amount
                        print('sender after:')
                        print(bank_list[i].balance)
                        print('receiver before:')
                        print(bank_list[j].balance)
                        bank_list[j].balance += amount
                        print('receiver after:')
                        print(bank_list[j].balance)
    else:
        print('Invalid input')

valid = False 
while valid == False:
    user_input = int(input('Please input your bank id : '))
    valid = check_validity(user_input)
    if valid: 
        action_input = input('What would you like to do - See Transactions / Withdraw / Deposit / Transfer Funds : ').lower() 
        if (action_input == 'withdraw' or action_input == 'deposit'):
            amount = int(input(f'Please enter the amount you want to {action_input} : '))
            # Check if there is sufficient amount
            if check_amt(amount, user_input, action_input):
                print('You can continue')
                # Transact the amount
                transact(amount, action_input, user_input, '')
            else:
                print('You have insufficient Fund')
        elif (action_input == 'transfer') :
            amount = int(input(f'Please enter the amount you want to {action_input} : '))
            # Check if there is sufficient amount
            if check_amt(amount, user_input.lower(), action_input):
                account_id = int(input('Please enter account number to transfer to : '))
                while check_validity(account_id) == False:
                    print('Incorrect Account ID')
                    account_id = int(input('Please enter account number to transfer to : '))
                transact(amount, action_input, user_input, account_id)
                # if check_validity(account_id):
                #     # Transact the amount
                #     transact(amount, action_input, user_input, account_id)
                # else:
                #     print('Incorrect Account ID')
                #     account_id = int(input('Please enter account number to transfer to : '))
            else:
                print('You have insufficient Fund')
        elif(action_input == 'see transactions'):
            print('See transactions')
        else:
            print('False')
    else: 
    # If Bank ID is incorrect
    #if valid == False:
        print('Invalid ID, please try again later!')
