#Python for Everyone Projects > Arithmatic Adders
# Solution used: set 4 lines of strings and measure placement to order in console
from ast import operator

#Finding the largest string in the set
def get_largest_string(array_split):
    d = 0
    pp = 0
    isSame = False
    for c in array_split :
        try : 
            convInt = int(c)
        except :
            #print("its all ok man")
            pass

        if(isinstance(convInt, (int, float))) :
            if (d == len(c)) :
                isSame = True
            if (d < len(c)) :
                d = len(c)
                isSame = False
                if (pp == 0) :
                    isTop = True
                if (pp == 2) :
                    isTop = False
            if (d > len(c)) : 
                isSame = False
        pp += 1
    return d, isTop, isSame

def actual_Operator(array_Split):
    x1 = int(array_Split[0])
    op = array_Split[1]
    x2 = int(array_Split[2])
    total = 0
    try : 
        if(op == '+'):
            total = x1 + x2
        elif(op == '-'):
            total = x1 - x2
        else:
            print("what the hek mang")
    except :
        print("its not ok man")
    return total

def arithmetic_arranger(adders, input):
    
    if(input) :
        #print("true")

        try : 
            #Setting up each line, and some helpful variables
            line1 = ""
            line2 = ""
            line3 = ""
            line4 = ""
            tempStr = ""
            bumper = "   " #bumper is space between each equation -> note, changes to this will need to be changed in Line 4 as well

            #Looping thru dat array of strings to operate
            for a in adders :
                adderHeHe = 0
                statement = a.split()
                
                #Calling the 2 defined functions
                actualValue = str(actual_Operator(statement))
                getReturn = get_largest_string(statement)
                bigStr = getReturn[0]
                isTop = getReturn[1]
                isSame = getReturn[2]

                #Note: Lines are done out of order as 3rd line is the reference point for all the other ones
                #Line 3: Finding and setting the length of the bars (or equal sign)
                bar = ""
                if(isTop and isSame != True):
                        for x in range(bigStr + 1):
                            adderHeHe += 1
                            bar = bar + "-"
                elif(isSame == True):
                    for x in range(bigStr + 2):
                        adderHeHe += 1
                        bar = bar + "-"
                elif(isTop != True):
                    for x in range(bigStr + 2):
                        adderHeHe += 1
                        bar = bar + "-"
                bar =  bumper + bar
                y = 0
                line3 = line3 + bar

                #Line 4: Finding the space needed for Value output (actual solved value)
                z = adderHeHe - len(actualValue)
                tempStr = ""
                if (z > 0) : 
                    for xx in range(z):
                        tempStr = tempStr + " "
                if (z < 0) :
                    bumper = "  " #special overflow bumper
                line4 = line4 + bumper + tempStr + actualValue
                bumper = "   " #resetting just in case of overflow bumper
                
                #looping through each individual equation
                for b in statement :

                    #Spacing the Line 1: the 1st value of all eqns
                    if (y == 0) :
                        z = adderHeHe - len(b)
                        tempStr = ""
                        if (z > 0) : 
                            for xx in range(z):
                                tempStr = tempStr + " "
                        line1 = line1 + bumper + tempStr + b
                    
                    #Spacing Line 2: operator and the 2nd value of all eqns
                    if (y == 1) :
                        line2 = line2 + bumper + b
                    if (y == 2) :
                        z = bigStr - len(b) - 1
                        tempStr = ""
                        if (z > 0) : 
                            for xx in range(z):
                                tempStr = tempStr + " "
                        line2 = line2 + tempStr + " " + b
                    y += 1
                    #print(bar)
            # for SOE view:
            print(a + " = " + actualValue)
            
            #print(adders)
            #print(input)
        
        except : 
            print("error1")

    else : 
                        

        print("Select True in order to view out puts")
    if(input):
        print("\n" + line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n")

#print statements to test different sets
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

#added additional feature to take in negative ints:
arithmetic_arranger(["1 - -2"], True)

#add input here:
#arithmetic_arranger(["x - y", "x1 + y1"], True)