import string
import sys

print("Welcome to Vladimir's BMI Calculator")

# Prompt user for their name
sName = input("Please enter name of person who's BMI is being calculated: ")

# Prompt user to select their height unit
nCaseHeight = int(input("Select unit of height, enter 1 for inches, 2 for meters, 3 for feet, 4 for feet-inches: "))

# Set the conversion factor for each height unit
if nCaseHeight == 1:
    sHeightUnit = "inches"
    nConFactHeight = 0.0254
elif nCaseHeight == 2:
    sHeightUnit = "meters"
    nConFactHeight = 1
elif nCaseHeight == 3:
    sHeightUnit = "feet"
    nConFactHeight = 0.3048
elif nCaseHeight == 4:
    sHeightUnit = "feet-inches"
    nConFactHeight = 0
else:
    print("Error please only input numbers 1-4")
    sys.exit()

# Prompt user to select their weight unit
nCaseWeight = int(input("Select unit of weight: enter 1 for pounds, 2 for kilograms: "))

# Set the conversion factor for each weight unit
if nCaseWeight == 1:
    sWeightUnit = "pounds"
    nConFactWeight = 0.453592
elif nCaseWeight == 2:
    sWeightUnit = "kilograms"
    nConFactWeight = 1
else:
    print("Error please only input numbers 1 or 2")
    sys.exit()

# Prompt user for their weight and height
sHeight = input("Please supply their height in " + sHeightUnit + ": ")
nWeight = int(input("Please supply their weight in " + sWeightUnit + ": "))

# If the user selected feet-inches parse it to feet and inches and convert to inches
if nConFactHeight == 0:
    nHeight = int(sHeight[:sHeight.index('-')])*12+int(sHeight[sHeight.index('-')+1:])
    nConFactHeight = 0.0254
else:
    nHeight = int(sHeight)

# Convert height and weight
nHeightMeters = nHeight * nConFactHeight
nWeightKilos = nWeight * nConFactWeight

# Calculate BMI
nBMI = nWeightKilos/(nHeightMeters**2)

# Find BMI health status
if nBMI <= 18.5:
    sBMIStatus = "Underweight"
elif nBMI <= 24.9:
    sBMIStatus = "Normal"
elif nBMI <= 29.90:
    sBMIStatus = "Overweight"
else:
    sBMIStatus = "Obese"

# Output results to user
print(sName, "'s BMI is", "{:.2f}".format(nBMI))
print(sName, "'s BMI status is", sBMIStatus)
