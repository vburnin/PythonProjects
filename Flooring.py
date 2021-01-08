# Flooring calculator

# 1.Input both the Length and Width:

nLength = float(input("What is the length? "))
nWidth = float(input("What is the width? "))

# 2. Calculate
# 2.1 Area is Length x Width

nArea = nLength*nWidth

# 2.2 Scrap is 10% of the calculated area:

nScrap = nArea*0.1

# 2.2 Total is Area + Scrap
nTotal = nArea + nScrap

# 3. Output:
#    Area of the room:
#    Scrap value:
#    Total of Area + Scrap:
#    Total Square Yards which is Total / 9

print(format("Area of the room: ", "30s"), format(nArea, "10,.2f"))
print(format("Scrap value: ", "30s"), format(nScrap, "10,.2f"))
print(format("Total of Area + Scrap: ", "30s"), format(nTotal, "10,.2f"))
print(format("Total Square Yards: ", "30s"), format(nTotal/9, "10,.2f"))

value1 = 2.0
value2 = 12
print(format(value1 * value2, .3f)