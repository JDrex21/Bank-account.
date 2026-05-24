balance = 1000 #this is your initial balance
n = 0
#Now choose the service here
while 1>n :
    print("Enter your choice: \n1. Check Balance\n2. Deposit\n3. Withdrawl\n4. Exit")
    a = int(input())

    match a:
        case 1:
            print("\nYour balance is: ₹", balance) #case 1 to show balance
            print(" \n")
        case 2:
            depo = int(input("\nEnter deposit amount: ₹")) #case 2 to deposit
            print(" \n")
            balance = balance + depo
        
        case 3:
            wit = int(input("\nEnter withdrawl amount: ₹")) #case 3 to withdraw
            while wit <= balance:
                print(" \n")
                balance = balance - wit #case3 if the withdraw amount < balance
                break #break the while loop after deposition
            else:
                print("\nInsufficient Balance!\nTransiction Failed\n \n") #if wihdraw amount > balance
            
        
        case 4:
            print("\nThank You for using our Service ❤ \n")
            n=2 #case 4 exit the base while loop putting n=2, 1>n become fasle

        case _:
            print("\nInvalid output!\nPlease Choose again\n") #default case if you input anything beyond 1,2,3,4.

# Thank u for viewing my so tiny code....
