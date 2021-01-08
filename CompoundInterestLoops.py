import locale

locale.setlocale(locale.LC_ALL, '')

# Declare Variables
nDeposit = -1
nMonths = -1
nRate = -1
nGoal = -1
nCurrentMonth = 1

# Prompt user for input, check input to make sure its numerical
while nDeposit <= 0:
    try:
        nDeposit = int(input("What is the Original Deposit (positive value): "))
    except ValueError:
        print("Input must be a positive numeric value")
    if nDeposit <= 0:
        print("Input must be a positive numeric value")

while nRate <= 0:
    try:
        nRate = float(input("What is the Interest Rate (positive value): "))
    except ValueError:
        print("Input must be a positive numeric value")
    if nRate <= 0:
        print("Input must be a positive numeric value")

while nMonths <= 0:
    try:
        nMonths = int(input("What is the Number of Months (positive value): "))
    except ValueError:
        print("Input must be a positive numeric value")
    if nMonths <= 0:
        print("Input must be a positive numeric value")

while nGoal < 0:
    try:
        nGoal = int(input("What is the Goal Amount (can enter 0 but not negative): "))
    except ValueError:
        print("Input must be zero or greater")
    if nGoal < 0:
        print("Input must be zero or greater")

# Calculate Monthly Rate and save deposit for second loop
nMonthRate = nRate * 0.01 / 12
nAccountBalance = nDeposit

# For each month output the month and the current balance to screen
while nCurrentMonth <= nMonths:
    nAccountBalance += nAccountBalance * nMonthRate
    print("Month:", nCurrentMonth, "Account Balance is:", locale.currency(nAccountBalance))
    nCurrentMonth += 1

# Reset Month Counter
nCurrentMonth = 0

# Find amount of months it will take to reach goal by looping monthly calculation until goal reached
while nGoal > nDeposit:
    nDeposit += nDeposit * nMonthRate
    nCurrentMonth += 1

# Output the amount of months it would take to reach the goal and the goal
print("It will take:", nCurrentMonth, "months to reach the goal of", locale.currency(nGoal))
