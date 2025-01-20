# class myClass:
#     pass

class employee():
    
    deptName = "IT"
    
    def __init__(self, name, salary):
        self.empName = name
        self.empSalary = salary
    
    def get_employee(self):
        return f"{self.empName} salary is {self.empSalary}"
    

# arvind_instance = employee("Arvind", 30000)
# print(arvind_instance.deptName)

# balaji_instance = employee("Balaji", 50000)
# print(balaji_instance.get_employee())

class Bank:
    
    __balance = 0  # private variable
    
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        
    def __deposit(self, amount):  # --> private method
        self.__balance += amount
    
    def get_balance(self):
        self.__deposit(self.amount)
        print(f"{self.name} account balance is: {self.__balance}")
        

sandeep_account = Bank("Sandeep", 20000)
sandeep_account.get_balance()
# sandeep_account.__deposit()




        

