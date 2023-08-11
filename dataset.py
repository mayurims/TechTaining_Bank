from classes import account, customer

#customer_list = []
bank_list = []
transactions = []

bank_list.append(customer(1, 'Mayuri', 0))
bank_list.append(customer(2, 'Mig', 0))

# transactions.append(transactions(1, 100, 'withdraw'))

#print(bank_list)

valid = False
while valid == False:
    user_input = int(input('Please input your bank id : '))
    # Check validity of Bank ID
    for i in range(len(bank_list)):
        if user_input == bank_list[i].bank_id:
            print('Correct ID')
            valid = True
            action_input = input('What would you like to do - See Transactions / Withdraw / Deposit / Transfer Funds : ')        
    
    # If Bank ID is incorrect
    if valid == False:
        print('Invalid ID, please try again later!')
