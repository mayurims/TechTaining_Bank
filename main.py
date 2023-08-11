from classes import account, customer

#customer_list = []
bank_list = []
transactions = []

bank_list.append(customer(1, 'Mayuri', 0))
bank_list.append(customer(2, 'Mig', 0))

# transactions.append(transactions(1, 100, 'withdraw'))

#print(bank_list)

#user_input = int(input('Please input your bank id : '))
# Check validity of Bank ID
valid = False

def options():
    action_input = input('What would you like to do - See Transactions / Withdraw / Deposit / Transfer Funds : ')   

def check_validity(user_input):
    for i in range(len(bank_list)):
        if user_input == bank_list[i].bank_id:
            print('Correct ID')
            valid = True
            return valid
    return False


while valid == False:
    user_input = int(input('Please input your bank id : '))
    valid = check_validity(user_input)
    if valid: 
           action_input = input('What would you like to do - See Transactions / Withdraw / Deposit / Transfer Funds : ')   
    else: 
    # If Bank ID is incorrect
    #if valid == False:
        print('Invalid ID, please try again later!')
