#  The working process of ATM.

print("welcome to abc bank\n\nInsert your ATM card")

passward=1234
balance=10000
choice=0
pin=int(input("enter your name four digit pin\n"))
if pin==passward:
    while choice != 4:
        print("\n\n**** Menu ****")
        print("1 == blance")
        print("2 == deposit")
        print("3 == withdraw")
        print("4 == cancel\n")

        choice=int(input("enter your option:\n"))

        if choice==1:
            print("Blance = R",balance)

        elif choice==2:
            dep=int(input("Enteryour deposit amount: Rs"))
            balance += dep
            print("\n deposited amount:R" ,dep)
            print("blance = Rs", balance)

        elif choice==3:
            wit=int(input("Enteryour withroaw amount: R"))
            balance -= wit
            print("\n withdraw amount:Rs" ,wit)
            print("blance = Rs", balance)

        elif choice==4:
            print("\nsession ended !! Goodbye")
else:
    print("pin Incorrect !! try again")