#budget_app



from functools import total_ordering
from math import dist
from threading import activeCount
from tkinter import Y

#proper round, from: https://stackoverflow.com/questions/31818050/round-number-to-nearest-integer
# didn't end up using, but nice to have
def proper_round(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
        return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
    return float(num[:-1])

#Create spend chart
def create_spend_chart(lit):
    total = 0
    cat_total = []
    distr_list = []
    chart_list = []
    i = 0
    
    for l in lit:
        for trans in l.ledger:
            if(trans[2] == "Withdraw"):
                cat_total.append([0, "", 0])
                cat_total[i] = [float(trans[0]), l.name, ""]
        i += 1
    x = 0
    while (x < len(cat_total)):
        if(len(cat_total) != 0):
            total += cat_total[x][0]
        x += 1
    if(float(total) == 0.0):
        return print("You have not spent anything")



    for x in range(len(cat_total)):
        distr_list.append([0, "", 0])

    for l in lit:
        for p in cat_total:
            if(p[1] == l.name):
                for x in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
                    if((p[0]/total)*100 >= x-5):
                        p[2] = str(x)
    j = 0
    for x in [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]:
        if(len(str(x)) == 3): chart_list.append(str(x) + "| ")
        elif(len(str(x)) == 2): chart_list.append(" " + str(x) + "| ")
        elif(len(str(x)) == 1): chart_list.append("  " + str(x) + "| ")
        else: return print("Problem with printing chart.")
        for l in lit:
            noCat = True
            for c in cat_total:
                if(c[1] == l.name):
                    noCat = False
                    if(float(c[2]) >= float(x)):
                        chart_list[j] = chart_list[j] + "o  "
                    else:
                        chart_list[j] = chart_list[j] + "   "
            if(noCat):
                chart_list[j] = chart_list[j] + "   "
        j += 1
    chart_list.append("    -")
    for x in range(len(lit)):
        chart_list[j] = chart_list[j] + "---"

    maxChar = 0
    for l in lit:
        if(len(l.name) > maxChar):
            maxChar = len(l.name)
    j += 1
    i = 0
    for x in range(maxChar):
        chart_list.append("     ")
        for l in lit:
            if(len(l.name) < i + 1):
                chart_list[j] = chart_list[j] + "   "
            else:
                chart_list[j] = chart_list[j] + l.name[i] + "  "
        i += 1
        j += 1
    
    print("\nPercent spent by category")
    for c in chart_list:
        print(c)

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
    
    def withdraw(self, amm, desc = ""):
        if(self.total_ammount > float(amm)):
            self.total_ammount -= float(amm)
            self.ledger.append((amm, desc, "Withdraw"))
            self.ledger1.append(fix_it_felix(True, desc, amm))
        else:
            print("Unsuccessful Withdrawal: Not enough funds remaining in account.")
            return False

    def get_balance(self):
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


lst = []

# lst.append(Category("food"))
# lst.append(Category("clothing"))
# lst.append(Category("entertainment"))

# lst[0].deposit(1000)
# lst[1].deposit(200)
# lst[2].deposit(100)

# lst[0].transfer(140, lst[1])

# print(lst[1].total_ammount)
# print(lst[0].total_ammount)

# lst[0].withdraw(500)
# lst[1].withdraw(100)
# lst[2].withdraw(50)

#Just for fun, some inputs -> incompleted
while True:
    val = input("\nWhat would you like to do sonny? \n1. Find existing accounts \n2. Create new account\n3. View Transaction History\n4. Generate a Spent Chart \n [Enter an integer]: ")
    if(val == ""):
        break
    elif(val == "1"):
        print("\nExisting accounts:")
        i = 1
        for l in lst:
            print("    ", str(i), ". ", l.name)
            i += 1
        val2 = input("Select an account to view [Press 'Enter' to escape, or enter an integer]: ")
        val3 = input("\nWhat would you like to do to with \"" + lst[int(val2)-1].name + "\"?\n1. Deposit \n2. Withdraw\n3. Transfer\n4. Get Balance\n5. Check Funds\n[Press 'Enter' to escape, or enter an integer]: ")
        if(val3 == "1"):
            input1 = input("\nHow much would you like to Deposit?  ")
            input2 = input("Enter a description:  ")
            lst[int(val2)-1].deposit(input1, input2)
        elif(val3 == "2"):
            input1 = input("\nHow much would you like to Withdraw?  ")
            input2 = input("Enter a description:  ")
            lst[int(val2)-1].withdraw(input1, input2)
        elif(val3 == "3"):
            nameSel = lst[int(val2)-1].name
            i = 1
            print("\nOther accounts:")
            for l in lst:
                if(l.name != nameSel):
                    print("    ", str(i), ". ", l.name)
                i += 1
            input1 = input("\nWhich account would you like to transfer to? \n[Enter an integer]:   ")
            input2 = input("\nHow much would you like to transfer?  ")
            lst[int(val2)-1].transfer(input2, lst[int(input1)-1])
        elif(val3 == "4"):
            print(lst[int(val2)-1].get_balance())
        elif(val3 == "5"):
            input1 = input("Enter an ammount to check:  ")
            print(str(lst[int(val2)-1].check_funds(input1)))
    elif(val == "2"):
        newVal = input("enter a name")
        if(newVal == ""):
            print("Invalid Entry")
        else:
            lst.append(Category(newVal))
    elif(val == "3"):
        i = 1
        print("\nExisting accounts:")
        for l in lst:
            print("    ", str(i), ". ", l.name)
            i += 1
        inp3 = input("\n[Enter an integer]: ")
        print("\n")
        try: 
            for l in(lst[int(inp3)-1].ledger1):
                print(str(l))
        except:
            print("Invalid Entry")
    elif(val == "4"):
        create_spend_chart(lst)
        print("\n")
    else:
        print("Invalid Entry")

