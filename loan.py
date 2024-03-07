#Get details of loan
money_owed=float(input("Enter the amount owed by you:\n"))#2000
apr=float(input("What is annual percentage rate:\n "))
payments=float(input("How much will you pay each months:\n"))
months=int(input("For how many months will you want to see the results for:\n"))

monthly_rate=apr/100/12

for i in range(months):
    #Interest paid 
    interest_paid=money_owed*monthly_rate
    #Add in Interest
    money_owed=money_owed+interest_paid
    #Make payments
    if (money_owed-payments>0):
        print("The money owed",money_owed)
        print("You paid your loan in",i+1,'months' )
        break
    money_owed=money_owed-payments

    print('Paid',payments,'of which',interest_paid,'was interest',end=' ')
    print('Now I owe',money_owed)