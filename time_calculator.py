# Time Calculator

from ast import Raise
from math import remainder


def calculate_time(curTime, addedTime):
    #set up bools
    flipAM_PM = False
    
    #Set up Current Time Array and Added Time Array
    temp1Array = curTime.split()
    temp2Array = temp1Array[0].split(':')
    timeArray = temp2Array
    timeArray.append(temp1Array[1])
    addTimeArray = addedTime.split(':')
    isPM = False

    try:
        hr1 = timeArray[0]
        if(hr1 == '12'):
            hr1 = '00'
        mn1 = timeArray[1]
        ap1 = timeArray[2]
        if(ap1.lower() == "pm"):
            isPM = True
        hr2 = addTimeArray[0]
        mn2 = addTimeArray[1]

        #Some hard-coded error checking
        if(len(mn1) > 2 or len(mn1) < 2 or len(hr1) > 2 or len(hr1) < 1 or len(ap1) > 2 or len(ap1) < 2 or int(hr1) > 12 or int(mn1) > 60):
            #break if incorrect format
            raise NameError("Format Error")
        
        #Find Minutes
        mn3 = int(mn1) + int(mn2)
        remainMN = mn3 % 60
        carryMn = (mn3 / 60) - (remainMN / 60)
        finalMN = int(remainMN)

        #Find Hours
        hr3 = int(hr1) + int(hr2) + carryMn
        remainHR = hr3 % 12
        carryHr = (hr3 / 12) - (remainHR / 12)
        finalHr = int(remainHR)
        if(finalHr == 0):
            finalHr = 12

        #Find AM/PM Shift
        am_pmChange = carryHr % 2
        if(am_pmChange != 0):
            print("this is a change in AM or PM")
            if(ap1.lower() == "am"):
                ap1 = "PM"
            elif(ap1.lower() == "pm"):
                ap1 = "AM"
            else:
                raise NameError("Bad AM/PM choice")
        else:
            ap1 = ap1.upper()
        #Find Day Shift
        carryTwelve = hr3
        if(ap1.lower() != "am" and ap1.lower() != "pm"):
            raise NameError("Bad AM/PM choice")
        if(isPM):
            carryTwelve = carryTwelve + 12
        remainDay = carryTwelve % 24
        carryDay = (carryTwelve - remainDay) / 24
        finalDay = int(carryDay)

        return finalHr, finalMN, ap1, finalDay

    except:
        print("There was an error with how the dates were written, please use the correct format.")

    print(timeArray)


def output_time(newTime, carriedDays):
    print("fnc2")

#time = input("What is the current time?\n    (Format => HH:MM AM/PM) \n")
#addTime = input("How much time would you like to add?\n    (Format => *H:MM) *you may add more than 1 digit worth of hours \n")
#dayInput = input("Specific weekday?\n   Note: If none, press 'Enter'\n")

time = "10:20 pm"
addTime = "32:50"

effort = calculate_time(time, addTime)
try:
    print(effort)
except:
    ("Bad Return")