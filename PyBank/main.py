import os
import csv

#Assign variables  
total_months = 0 
total_revenue = 0 
previous_revenue = 0
greatest_increase = 0
greatest_decrease = 0 
increase_month = ""
decrease_month = ""

#Create lists 
list_of_changes = []
months = []
 



#Path to collect data from the Resources folder & open CSV file
CSVpath = os.path.join('Resources', 'budget_data.csv')
with open(CSVpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter= ',')
    
    #Skip the header row
    next(csv_reader, None)
  

    for rows in csv_reader: 
        
        #Calculate the total number of months included in dataset
        total_months = total_months + 1

        #Calculate the net total amount of profit/losses over the entire period 
        total_revenue = total_revenue + int(rows[1])

        #Calculate the average of changes in profit/losses over the entire period
        revenue_change =  int(rows[1]) - previous_revenue 
        if total_months != 1:
            list_of_changes.append(revenue_change)
        
        previous_revenue = int(rows[1])

       
         #Creating a list of months
        months.append(rows[0])
   

    #Find the greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(list_of_changes)
    increase_month = months[list_of_changes.index(greatest_increase) + 1]
   

    #Find the greatest decrease in losses (date and amount) over the entire period 
    greatest_decrease = min(list_of_changes)
    decrease_month = months[list_of_changes.index(greatest_decrease) + 1]
  
  
   
    #Calculate average_change outside of the for loop
    average_change = round(sum(list_of_changes)/len(list_of_changes),2)
   


#Print to terminal 
print("Financial Analysis")
print("--------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: $" + str(total_revenue))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " +str(increase_month) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " +str(decrease_month) + " ($" + str(greatest_decrease) + ")")


#Path to export file as textfile
export_file = os.path.join('Resources', "budget_data.txt")
with open(export_file, 'w') as textfile:
    textfile.write("Financial Analysis" "\n")
    textfile.write("--------------------------" "\n")
    textfile.write("Total Months: " + str(total_months) + "\n")
    textfile.write("Total Revenue: $" + str(total_revenue) + "\n")
    textfile.write("Average Change: $" + str(average_change) + "\n")
    textfile.write("Greatest Increase in Profits: " +str(increase_month) + " ($" + str(greatest_increase) + ")" +"\n")
    textfile.write("Greatest Decrease in Profits: " +str(decrease_month) + " ($" + str(greatest_decrease) + ")")