#budget_app



from functools import total_ordering
from threading import activeCount
from tkinter import Y

#function for printing out 30 character lines
def fix_it_felix(isMinus, x2, y):
    maxChar = 30
    remainingChars = 30

    x3 = str(y)
    if(type(y) == type(float(y))):
        x3t = x3.rstrip('.')
        if(len(x3t[1])):
            x3 += "0"
    if(type(y) == type(int(y))):
        x3 += ".00"
    if(isMinus):
        x3 = "-" + x3

    printLine = ""
    if(len(x3)<maxChar):
        if(len(x3)<remainingChars):
            remainingChars = remainingChars - len(x3) - 1
            printLine = " " + x3
        else:
            printLine = x3[0:remainingChars-1]

        if(remainingChars>0):
            if(len(x2)<remainingChars):
                    remainingChars -= len(x2)
                    for i in range(remainingChars + 1):
                        printLine = " " + printLine
                    printLine = x2 + printLine
        else:
            printLine = x2[0:remainingChars-1] + printLine
            
    else:
        remainingChars = 0
        printLine = x3[0:26] + "..."
    
    return printLine

class Category:
    
    name = ""
    #ledger.append("***************TRANSACTION HISTORY*******************")
    total_ammount = 0
    
    def __init__(self, z):
        self.name = z
        self.ledger = []
        self.ledger1 = []
        x = len(z)
        if(x<30):
            string1 = ""
            if(x%2 != 0):
                for i in range(int((30-x-1)/2)):
                    string1 = string1 + "*"
                self.ledger.append(string1 + z + string1 + "*")
                self.ledger1.append(string1 + z + string1 + "*")
            else:
                for i in range(int((30-x)/2)):
                    string1 = string1 + "*"
                self.ledger.append(string1 + z + string1)
                self.ledger1.append(string1 + z + string1 + "*")
        else:
            self.ledger.append(z[0:29])
            self.ledger1.append(z[0:29])
        print(self.name, "constructed")
    
    def deposit(self, amm, desc = ""):
        self.total_ammount += float(amm)
        self.ledger.append((amm, desc, "Deposit"))
        self.ledger1.append(fix_it_felix(False, desc, amm))
        #print(self.name, "remaining moneys: ", self.total_ammount)
    
    def withdraw(self, amm, desc = ""):
        if(self.total_ammount > float(amm)):
            self.total_ammount -= float(amm)
            self.ledger.append((amm, desc, "Withdraw"))
            self.ledger1.append(fix_it_felix(True, desc, amm))
            #print(self.name, "has withdrawn: -" + amm + " dollars")
        else:
            print("Unsuccessful Withdrawal: Not enough funds remaining in account.")
            return False

    def get_balance(self):
        #print(self.name +":", self.total_ammount)
        return str(fix_it_felix(False, "Ammount remaining:", self.total_ammount))
        

    def transfer(self, amm, target):
        try:
            if(self.total_ammount >= float(amm)):
                print("Transfer to " + target.name)
                target.total_ammount += float(amm)
                self.total_ammount -= float(amm)
                self.ledger.append((amm, "from: "+ self.name + " to: " + target.name, "Transferred"))
                self.ledger1.append(fix_it_felix(True, "Transfer to " + target.name, amm))
                target.ledger1.append(fix_it_felix(False, "Transfer from " + self.name, amm))
            else:
                print("insufficient funds")
        except:
            print("invalid account transfer")

    def check_funds(self, amm):
        if(self.total_ammount < float(amm)):
            return False
        else:
            return True


list = []



list.append(Category("food"))
list.append(Category("clothing"))
list.append(Category("entertainment"))

list[0].deposit(1000)
list[1].deposit(200)
list[2].deposit(100)

list[0].transfer(140, list[1])

print(list[1].total_ammount)
print(list[0].total_ammount)


#Just for fun, some inputs -> incompleted
while True:
    val = input("\nWhat would you like to do sonny? \n1. Find existing accounts \n2. Create new account\n3. View Transaction History \n [Enter an integer]: ")
    if(val == ""):
        break
    elif(val == "1"):
        print("\nExisting accounts:")
        i = 1
        for l in list:
            print("    ", str(i), ". ", l.name)
            i += 1
        val2 = input("Select an account to view [Press 'Enter' to escape, or enter an integer]: ")
        val3 = input("\nWhat would you like to do to with \"" + list[int(val2)-1].name + "\"?\n1. Deposit \n2. Withdraw\n3. Transfer\n4. Get Balance\n5. Check Funds\n[Press 'Enter' to escape, or enter an integer]: ")
        if(val3 == "1"):
            input1 = input("\nHow much would you like to Deposit?  ")
            input2 = input("Enter a description:  ")
            list[int(val3)-1].deposit(input1, input2)
        elif(val3 == "2"):
            input1 = input("\nHow much would you like to Withdraw?  ")
            input2 = input("Enter a description:  ")
            list[int(val3)-1].withdraw(input1, input2)
        elif(val3 == "3"):
            nameSel = list[int(val2)-1].name
            i = 1
            print("\nOther accounts:")
            for l in list:
                if(l.name != nameSel):
                    print("    ", str(i), ". ", l.name)
                i += 1
            input1 = input("\nWhich account would you like to transfer to? \n[Enter an integer]:   ")
            input2 = input("\nHow much would you like to transfer?  ")
            list[int(val3)-1].transfer(input2, list[int(input1)-1])
        elif(val3 == "4"):
            print(list[int(val2)-1].get_balance())
        elif(val3 == "5"):
            input1 = input("Enter an ammount to check:  ")
            print(str(list[int(val2)-1].check_funds(input1)))
    elif(val == "2"):
        newVal = input("enter a name")
        if(newVal == ""):
            print("Invalid Entry")
        else:
            list.append(Category(newVal))
    elif(val == "3"):
        i = 1
        print("\nExisting accounts:")
        for l in list:
            print("    ", str(i), ". ", l.name)
            i += 1
        inp3 = input("\n[Enter an integer]: ")
        print("\n")
        try: 
            for l in(list[int(inp3)-1].ledger1):
                print(str(l))
        except:
            print("Invalid Entry")
        # for l in(list[0].ledger):
        #     print(str(l[0]) + " " + str(l[1]) + " " + str(l[2]))
    else:
        print("Invalid Entry")

# try: input("gimme stuff to do: ")

# except:
#     print("oopsies")

