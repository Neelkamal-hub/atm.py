print('Welcome to ATM by python')
restart=('Y')
chances = 3
balance = 999.12
while chances >= 0:
    pin = int(input('Please enter your 4 Digit Pin :'))
    if pin == (1234):
        print('You entered your pin correctly')
        print('Please Press 1 For your Balance')
        print('Please Press 2 To make withdrawal')
        print('Please Press 3 To Pay in')
        print('Please Press 4 To Return Card \n')

        while restart not in ('n','NO','no','N'):
            print('Please Press 1 For your Balance')
            print('Please Press 2 To make withdrawal')
            print('Please Press 3 To Pay in')
            print('Please Press 4 To Return Card')
            option = int(input('What would you like to choose?: '))
            if option == 1:
                print('Your balance is $',balance)
                restart = input('Would you like to go back ? ')
                if restart in ('n','NO','no','N'):
                    print('Thankyou')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawal = float(input('How much would you like to withdraw ? 10,20,40,60,80,100 for other enter 1:'))

                if withdrawal in [10,20,40,60,80,100]:
                     balance = balance - withdrawal
                     print('\n Your Balance is now $',balance)
                     restart = input('Would you like to go back ?')
                     if restart in ('n','NO','no','N'):
                         print('Thankyou')
                         break
                elif withdrawal != [10,20,40,60,80,100]:
                    print('Invalid Amount, Please Try Agian \n')
                    restart = ('y')
                elif withdrawal == 1:
                    withdrawal = float(input('Please Enter Your Desired amount: '))
            elif option == 3:
                Pay_in = float(input('How much would you like to pay in?'))
                balance = balance + Pay_in
                print('\n Your Current Balance is $ ',balance)
                restart = input('Would you like to go back ?')
                if restart in ('n','NO','no','N'):
                    print('Thankyou')
                    break
                
            elif option == 4:
        
                print('Please wait whilst your card is returned.....\n')
                print('Thankyou for your service')
                break
            else:
                print('Please Enter a correct number \n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\n No more tries')
            break
        




