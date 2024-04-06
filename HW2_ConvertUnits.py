# File:     ConvertUnits.py
# Student:  Yejin Hong
# UT EID:   yh25396
# Course Name: CS303E
# 
# Date:     01/29/24
# Description of Program: This program prints english Units and metric Units of entered feet and inches

inputFeet = int( input("Enter number of feet: ") )
inputInches = int( input("Enter number of inches: ") )

def englishUnits():
    print("English Units")
    feet = inputFeet + inputInches/12
    inches = inputFeet*12 +inputInches
    yards = feet/3
    miles = feet/5280

    print(" feet: %g" %(feet))
    print(" inches: %d" %(inches))
    print(" yards: %f" %(yards))
    print(" miles: %f" %(miles))


def metricUnits():
    print("\nMetric Units")
    feet = inputFeet + inputInches/12
    meters = feet*(0.3048)
    centimeters = meters * 100
    millimeters = centimeters * 10
    kilometers = meters/1000
    print(" meters: %f" %(meters))
    print(" centimeters: %f" %(centimeters))
    print(" millimeters: %f" %(millimeters))
    print(" kilometers: %f" %(kilometers))

#print(inputFeet + " feet and " + inputInches + " equals: " +'\n')
print("\n%d feet and %d inches  equals: \n" %(inputFeet ,inputInches))


englishUnits()
metricUnits()
