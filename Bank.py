balance = 1000
n = 0
while 1>n :
    print("Enter your choice: \n1. Check Balance\n2. Deposit\n3. Withdrawl\n4. Exit")
    a = int(input())

    match a:
        case 1:
            print("\nYour balance is: ₹", balance)
            print(" \n")
        case 2:
            depo = int(input("\nEnter deposit amount: ₹"))
            print(" \n")
            balance = balance + depo
        
        case 3:
            wit = int(input("\nEnter withdrawl amount: ₹"))
            while wit <= balance:
                print(" \n")
                balance = balance - wit
                break
            else:
                print("\nInsufficient Balance!\nTransiction Failed\n \n")
            
        
        case 4:
            print("\nThank You for using our Service ❤ \n")
            n=2

        case _:
            print("\nInvalid output!\nPlease Choose again\n")