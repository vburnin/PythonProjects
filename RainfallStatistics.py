import plotly.express as px
import matplotlib.pyplot as plt

# getRainfallInput function takes a prompt and returns number user enters
def getRainfallInput(prompt):
    # Loop until user enters valid number
    while True:
        strInput = input(prompt)
        try:
            numInput = float(strInput)
            if numInput > 0:
                return numInput
            else:
                print("Please enter positive, non-zero number")
        except:
            print("Please enter a number")

def main():
    # Create tuple with every month
    tupMonths = (
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
    'December')
    # Create empty list to store rainfall averages
    lstRainfall = []
    # For every month get rainfall from user using getRainfallInput function and add it to lstRainfall list
    for strMonths in tupMonths:
        lstRainfall.append(getRainfallInput("Enter the rainfall for " + strMonths + ": "))
    # Find the sum, min and max rainfall and store them in variables
    numSumRainfall = sum(lstRainfall)
    numMinRainfall = min(lstRainfall)
    numMaxRainfall = max(lstRainfall)
    # Display sum, average, min and max to user
    print("Total rainfall:", format(numSumRainfall, ",.1f"))
    print("Average rainfall:", format(numSumRainfall/12, ",.1f"))
    print("Highest rainfall:", format(numMaxRainfall, ",.1f"), "in", tupMonths[lstRainfall.index(numMaxRainfall)])
    print("Lowest rainfall:", format(numMinRainfall, ",.1f"), "in", tupMonths[lstRainfall.index(numMinRainfall)])
    # Ask user which grpah option they want to use
    numGraphOption = input("1. Pyplot Bar Graph\n2. Pyplot Line Graph\n3. Pyplot Scatter Graph\n4. Plotly Bar Graph\n5. Plotly Line Graph\n6. Plotly Scatter Graph\n7. Plotly Pie Graph\nEnter graph option number or any other character to skip graphing: ")
    # Graph rainfall data using option user selected
    if numGraphOption == "1":
        plt.bar(tupMonths, lstRainfall)
        plt.xlabel("Month of the Year")
        plt.ylabel("Average Rainfall in Inches")
        plt.title("Bar Graph Rainfall Averages")
        plt.show()
    elif numGraphOption == "2":
        plt.scatter(tupMonths, lstRainfall)
        plt.xlabel("Month of the Year")
        plt.ylabel("Average Rainfall in Inches")
        plt.title("Scatter Graph Rainfall Averages")
        plt.show()
    elif numGraphOption == "3":
        plt.plot(tupMonths, lstRainfall)
        plt.xlabel("Month of the Year")
        plt.ylabel("Average Rainfall in Inches")
        plt.title("Line Graph Rainfall Averages")
        plt.show()
    elif numGraphOption == "4":
        fig = px.bar({"Month of the Year": tupMonths, "Average Rainfall in Inches": lstRainfall}, x="Month of the Year", y="Average Rainfall in Inches", title="Bar Graph Rainfall Averages")
        fig.show()
    elif numGraphOption == "5":
        fig = px.line({"Month of the Year": tupMonths, "Average Rainfall in Inches": lstRainfall}, x="Month of the Year", y="Average Rainfall in Inches", title="Line Graph Rainfall Averages")
        fig.show()
    elif numGraphOption == "6":
        fig = px.scatter({"Month of the Year": tupMonths, "Average Rainfall in Inches": lstRainfall}, x="Month of the Year", y="Average Rainfall in Inches", title="Scatter Graph Rainfall Averages")
        fig.show()
    elif numGraphOption == "7":
        fig = px.pie({"Month of the Year": tupMonths, "Average Rainfall in Inches": lstRainfall}, names="Month of the Year", values="Average Rainfall in Inches", title="Pie Graph Rainfall Averages")
        fig.show()
    else:
        print("Entered graph option not listed, exiting...")
main()