# This script opens a csv file and analyzes income data

# Modules
import os
import csv

# Path to collect data from budget_data.csv
budget_csv = os.path.join("budget_data.csv") 

#Initialize variables
months = 0
change_income = 0
income_changes = []
greatest_increase = 0 
greatest_decrease = 0  

# Open CSV
with open(budget_csv, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header and start at first row
    header = next(csvreader)
    firstrow = next(csvreader)
   
    # Assign variables
    total_income = int(firstrow[1])
    last_month_income = int(firstrow[1])
    months += 1

    #Loop through data 
    for row in csvreader:     
    
        # Output number of months
        months += 1
    
        # Sum total profit and losses
        total_income += int(row[1]) 

        # Find change in income and append to list of income changes 
        this_month_income = int(row[1])
        change_income = this_month_income - last_month_income
        income_changes.append(change_income)
        last_month_income = this_month_income

        #Find greatest increase and decrease in profits
        if change_income > greatest_increase:
            greatest_increase = change_income
            month_greatest_increase = row[0]
        if change_income < greatest_decrease:
            greatest_decrease = change_income
            month_greatest_decrease = row[0]

# Compute average change
average_change = round(sum(income_changes)/ (months-1),2)

# Print results to terminal
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total_income}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {month_greatest_increase} $({greatest_increase})")
print(f"Greatest Decrease in Profits: {month_greatest_decrease} $({greatest_decrease})")

# Export results to text file
results = open("budget_results.txt", "w+")        
results.write("Financial Analysis \n")
results.write("------------------------- \n")
results.write(f"Total Months: {months} \n")
results.write(f"Total: ${total_income} \n")
results.write(f"Average Change: ${average_change} \n")
results.write(f"Greatest Increase in Profits: {month_greatest_increase} $({greatest_increase}) \n")
results.write(f"Greatest Decrease in Profits: {month_greatest_decrease} $({greatest_decrease}) \n")