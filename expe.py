'''total=0
expenses=[]
for i in range(7):
    expenses.append(float(input("Enter your expenses:")))
total=sum(expenses)
print('Your total is $',total,sep='') 
'''
total=0
expenses=[]
num_expenses=int(input('Enter number of expenses:'))
for i in range(num_expenses):
    expenses.append(float(input("Enter your expenses:")))
total=sum(expenses)
print("Your total number of expenses is"+' '+ str(num_expenses) +' '+'and total is Rs',total,sep=' ')
