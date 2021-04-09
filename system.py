import random
class TooManyAttempt(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

class Bank_Account(TooManyAttempt):
                def __init__(self): 
                        self.balance=0
                        
                        

                def deposit(self):
                        y=int(input("If you want to Deposit Enter 1 For Next Enter 2:"))
                        print (" ")
                        if y==1:
                            amount=float(input("Enter amount to be Deposited: "))
                            if amount>=500:
                                self.balance += amount 
                                print("\n Amount Deposited:",amount)
                                print(" ")
                            else:
                                print(" ")
                                print("*"*5,"Minimum of Deposited Amount 500","*"*5)
                                print(" ")
                        elif y==2:
                            print("Next ")
                            print(" ")
                        else:
                            print("Please Enter Valid Option To Deposit")
                            

                def withdraw(self):
                        x=int(input("If you want to Withdraw enter 1 For Next Enter 2 :"))
                        print(" ")
                        if x==1:
                            amount = float(input("Enter amount to be Withdrawn: "))
                            if self.balance>=amount:
                                    if amount>=500:
                                            if amount<=10000:
                                                self.balance-=amount 
                                                print("\n You Withdrew:", amount)
                                                print(" ")
                                            else:
                                                print(" ")
                                                print("You Cannot Withdraw above 10000")
                                    else:
                                        print("You Cant Withdraw Below 500")
                                        print(" ")
                            else: 
                                    print("\n Insufficient balance ")
                                    print(" ")
                        elif x==2:
                            print("Next ")
                            print(" ")
                        else:
                            print("Please Enter Valid Option To Withdraw")

                def display(self): 
                        print("\n Net Available Balance=",self.balance)
                        print(" ")
                        print("Thank You For Banking With Us")
                        print("*"*3,self.name,"*"*3)

                def accountnumber(self):
                        randomlist = []
                        for i in range(0,16):
                            n= random. randint(0,9)
                            print(n,end=" ")
                        print("="*5,"Successfully Account Number Generated","="*5)
                        print(" ")

                def login(self):
                    print("Create a Username and Password for Login ")
                    print("Username in Alphabets and PIN in Numbers")
                    self.username = input(str("USERNAME : "))
                    self.password = input("PIN : ")
                    self.count = 0
                    try:
                        while True:
                            if self.count == 3:
                                raise TooManyAttempt("Account Blocked For 24hours")
                            u = input("UserID :")
                            p = input("PIN: ")
                            if (self.username==u and self.password==p):
                                print("Login Sucessfully")
                                print("#" * 5, "Welcome to the Deposit & Withdrawal Machine", "#" * 5)
                                print(" ")
                                print("*" * 10, self.name, "*" * 10)
                                print(" ")
                                break
                            else:
                                print("Invalid Credintals")
                                self.count += 1
                    except TooManyAttempt as tma:
                        print("access denied Mr/Mrs", self.name)
                        print(" ")
                        print(tma)
                        print("TOO MANY TIMES")
                        exit()


                def createaccountdetails(self):
                        print(" "*12,"Create a Account  STATE OF INDIA")
                        print("*"*3,"Fill Up Your Details","*"*3)
                        self.name=str(input("Enter the Name : "))
                        self.phNumber=int(input("Enter Your Phone Number : "))
                        self.accountType=str(input("Account Type SAVINGS or CURRENT : "))
                        self.branch=str(input("Enter Your Branch : "))
                        print(" ")
                        print("Sucessfully Account Created Mr/Mrs",self.name)
                        print(" ")
                        print("Hello!!! Welcome to State Bank of India ") 
                        print(" ")
                        
                        
                        
                        
                def accountdetails(self):
                        print("Name : ","*"*3,self.name,"*"*3)
                        print(" ")
                        print("PHONE NUMBER : ","*"*3,self.phNumber,"*"*3)
                        print(" ")
                        print("ACCOUNT BALANCE : 0 ")
                        print(" ")
                        print("ACCOUNT TYPE: ","*"*3,self.accountType,"*"*3)
                        print(" ")
                        print("BRANCH : ","*"*3,self.branch,"*"*3)
                        print(" ")
                    




                        
                                
                                                
                       

    

