# Prompt user for inputs

nPrincipal = float(input("Enter the starting principal: "))
nRate = float(input("Enter the annual interest rate: "))
nCompounds = int(input("How many times per year is the interest compounded? "))
nPeriods = int(input("For how many years will the account earn interest? "))

# Set grammar of output depending if years is plural
sYear = "Years"
if nPeriods == 1:
    sYear = "Year"

# Perform calculations and output to user
print("At the end of", nPeriods, sYear, "you will have $", format(nPrincipal*(1+nRate*0.01/nCompounds)**(nCompounds*nPeriods), ",.2f"))
