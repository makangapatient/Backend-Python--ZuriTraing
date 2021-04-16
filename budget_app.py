class Budget:

    def __init__(self,**categories):
        self.categories = categories
        print(self.categories)

    def deposit(self,amount,category):
        self.categories[category] = self.categories[category] + amount
        print('You deposited the sum of $'+str(amount)+' '+ 'to '+category)
        print('Your current balance is: ', self.categories[category])
    
    def withdraw(self,amount,category):
        if amount > self.categories[category]:
            print("Insufficient Balance")
        else:

            self.categories[category] = self.categories[category] - amount
            print('You withdrew the sum of $'+str(amount)+' from '+ category)
            print('Your current balance of is: ', self.categories[category])

    def transfer(self,amount,debitCategory,creditCategory):
        if amount > self.categories[debitCategory]:
            print('Insufficient Balance')
        else:
            self.categories[debitCategory] = self.categories[debitCategory] - amount
            self.categories[creditCategory] =  self.categories[creditCategory] + amount
            print('You transfered the sum of $'+ str(amount) + ' ' + 'from ' + debitCategory + ' to '+ creditCategory )
            print('The current balance of '+str(creditCategory)+' is: ', self.categories[creditCategory])
    
    def checkBalance(self,category):
        print('Your '+ category + ' budget balance is ' + str(self.categories[category]))
        
print('=== ===== ====== ====== ====== ====== ====== ===== ==== === =')
print('==== **** Current budget of each budget option ***** ==== ===')
print()
mybudget= Budget(food=100, clothing=200, rent=3000,entertainment=150)
print('=== ===== ====== ====== ====== ====== ====== ===== ==== === =')
print()
print('=== ===== ====== ====== ====== ====== ====== ===== ==== === =')
print('===== ==== **** Food deposit **** ======= ======= ===== === =')
mybudget.deposit(150, 'food')
print('=== ===== ====== ====== ====== ====== ====== ===== ==== === =')
print()
print('=== ===== ====== ====== ====== ====== ====== ===== ==== === =')
print('===== ==== **** Rent withdrawal ****  ====== ===== ==== === =')
mybudget.withdraw(50,'rent')
print('=== ===== ====== ====== ====== ====== ====== ===== ==== === =')
print()
print('=== ===== ====== ====== ====== ====== ====== ===== ==== === =')
print('===== ==== **** entertaiment And clothing transfer **** === =')
mybudget.transfer(70,'entertainment','clothing')
print('=== ===== ====== ====== ====== ====== ====== ===== ==== === =')
mybudget.checkBalance('clothing')
