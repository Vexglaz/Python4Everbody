# Time Calculator
from calendar import weekday
from cgi import test
import sys
from ast import Raise
from math import remainder


def calculate_time(curTime, addedTime, day = "Not Specified"):
    try:
        #set up bools
        dayInput = True
        if(day == "Not Specified"):
            dayInput = False
        
        #Set up Current Time Array and Added Time Array
        temp1Array = curTime.split()
        temp2Array = temp1Array[0].split(':')
        timeArray = temp2Array
        timeArray.append(temp1Array[1])
        addTimeArray = addedTime.split(':')
        isPM = False

        #Setting up time variables
        hr1 = timeArray[0]
        if(hr1 == '12'):
            hr1 = '00'
        mn1 = timeArray[1]
        ap1 = timeArray[2]
        if(ap1.lower() == "pm"):
            isPM = True
        hr2 = addTimeArray[0]
        mn2 = addTimeArray[1]
        daysLater = ""
        dayText = ""
        specDay = ""
        specDayInt = 0

        #Some hard-coded error checking
        if(len(mn1) > 2 or len(mn1) < 2 or len(hr1) > 2 or len(hr1) < 1 or len(ap1) > 2 or len(ap1) < 2 or int(hr1) > 12 or int(mn1) > 60):
            #break if incorrect format
            raise NameError("Format Error")
        
        #Find Minutes
        mn3 = int(mn1) + int(mn2)
        remainMN = mn3 % 60
        carryMn = (mn3 / 60) - (remainMN / 60)
        finalMN = int(remainMN)
        finalMin = str(finalMN)
        if(len(finalMin) == 1) :
            finalMin = "0" + str(finalMN)
        elif(len(finalMin) == 0) :
            finalMin = "00" + finalMN

        #Find Hours
        hr3 = int(hr1) + int(hr2) + carryMn
        remainHR = hr3 % 12
        carryHr = (hr3 / 12) - (remainHR / 12)
        finalHr = int(remainHR)
        if(finalHr == 0):
            finalHr = 12
        finalHour = str(finalHr)

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
        daysLater = int(carryDay)

        #Set up Day array and find if there is a new day
        if(dayInput):
            isHit = False
            weekdays = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
            for i in range(len(weekdays)) :
                d = weekdays[i]
                if(day.lower() == d):
                    isHit = True
                    #specDay = d
                    specDayInt = i
            if(isHit != True):
                raise NameError("Error: Make sure you correctly spelled the name of the day.")
            testDay = daysLater + specDayInt
            while(testDay > 6):
                testDay = testDay - 6
            specDay = weekdays[testDay]
            specDay = ", " + specDay[0].upper() + specDay[1:]
        
        #Find out how many days later it is
        if(daysLater == 1):
            dayText = "(next day)"
        elif(daysLater > 1):
            dayText = "(" + str(daysLater) + " days later)"
        

        return finalHour, finalMin, ap1, specDay, dayText, daysLater

    except IndexError:
        #For catching errors
        #print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        print("There was an error with how the dates were written, please use the correct format.")


time = input("What is the current time?\n    (Format => HH:MM AM/PM) \n")
addTime = input("How much time would you like to add?\n    (Format => *H:MM) *you may add more than 1 digit worth of hours \n")
dayInput = input("Specific weekday?\n   Note: If none, press 'Enter'\n")

#time = "6:30 PM"
#addTime = "205:12"
if(dayInput == ""):
    effort = calculate_time(time, addTime)
else:
    effort = calculate_time(time, addTime, dayInput)
try:
    #Debug Outputs
    # print(effort)
    print(str(effort[0]) + ":" + effort[1] + " " + effort[2] + "" + effort[3] + "" + " " + effort[4])
except:
    ("Bad Return")