from classes import account, customer, transaction
import random
from tabulate import tabulate

#customer_list = []
bank_list = []
transactions = []

bank_list.append(customer(1, 'Mayuri', 1000))
bank_list.append(customer(2, 'Mig', 350))
bank_list.append(customer(3, 'Timothee', 400))
bank_list.append(customer(4, 'Mig_the_annoying_person', 10))

trans_display = []

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
                if amount <= bank_list[i].balance:
                    return True
        return False
    else:
        return True

def transid_gen():
    num = 1
    if len(transactions) == 0:
        return 1
    for i in range(len(transactions)):
        if num == transactions[i].transaction_id:
            num += 1
    return num

def see_transact(bank_id):
    trans_display.clear()
    counter = 0
    for i in reversed(range(0,len(transactions))):
        if (bank_id == transactions[i].bank_id and counter <= 10):
            #print(transactions[i].transaction_id)
            trans_display.append(
                [transactions[i].date, transactions[i].transaction_id , transactions[i].bank_id, transactions[i].amount,
                 transactions[i].action, transactions[i].balance])
            counter += 1
    if len(trans_display) == 0:
        print('No previous transactions')
    else:
        #table
        trans_display.insert(0,
            ['Date', 'Transaction_ID', 'Bank_ID', 'Amount', 'Action', 'Balance']
        )
        print(tabulate(trans_display))


def transact(amount, action, bank_id, target_bank_id):
    #validate here or in outer function
    if action ==  'withdraw':
        #withdraw
        for i in range(len(bank_list)):
            if bank_id == bank_list[i].bank_id:
                bank_list[i].balance -= amount
                print('Current Balance: '+str(bank_list[i].balance))
                transactions.append(transaction(transid_gen(), bank_list[i].bank_id, '', amount, 'withdraw', bank_list[i].balance))

        #transactions.append
    elif action == 'deposit':
        #deposit
        for i in range(len(bank_list)):
            if bank_id == bank_list[i].bank_id:
                bank_list[i].balance += amount
                print('Current Balance: ' + str(bank_list[i].balance))
                transactions.append(transaction(transid_gen(), bank_list[i].bank_id, '', amount, 'deposit', bank_list[i].balance))
    elif action == 'transfer':
        #transfer
        for i in range(len(bank_list)):
            if bank_id == bank_list[i].bank_id:
                for j in range(len(bank_list)):
                    if target_bank_id == bank_list[j].bank_id:
                        print('Current Balance: ' + str(bank_list[i].balance))
                        transactions.append(transaction(transid_gen(), bank_list[i].bank_id, bank_list[j].bank_id, amount, 'transfer', bank_list[i].balance))
                        transactions.append(
                            transaction(transid_gen(), bank_list[j].bank_id, bank_list[i].bank_id, amount, 'transfer',
                                        bank_list[j].balance))

    else:
        print('Invalid input')

# Adding the Database
bank_list.append(customer(1, 'Mayuri', 1000))
bank_list.append(customer(2, 'Mig', 350))
bank_list.append(customer(3, 'Timothee', 400))
bank_list.append(customer(4, 'Mig_the_annoying_person', 10))

transactions.append(transaction(transid_gen(), 1, '', 100, 'withdraw', 100))
transactions.append(transaction(transid_gen(), 1, '', 200, 'withdraw', 200))
transactions.append(transaction(transid_gen(), 2, '', 50, 'deposit', 50))

valid = False

while valid == False:
    user_input = int(input('Please input your bank id : '))
    valid = check_validity(user_input)
    if valid:
        #MENU
        action_input = input('What would you like to do - See Transactions / Withdraw / Deposit / Transfer Funds / Exit : ').lower()
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
            if check_amt(amount, user_input, action_input):
                account_id = int(input('Please enter account number to transfer to : '))
                while check_validity(account_id) == False:
                    print('Incorrect Account ID')
                    account_id = int(input('Please enter account number to transfer to : '))
                transact(amount, action_input, user_input, account_id)
            else:
                print('You have insufficient Fund')
        elif(action_input == 'see transactions'):
            see_transact(user_input)
        elif(action_input == 'exit'):
            print('Exit')
            break
        else:
            print('False')
        valid = False
        user_input = ''
    else:
    # If Bank ID is incorrect
    #if valid == False:
        print('Invalid ID, please try again later!')
