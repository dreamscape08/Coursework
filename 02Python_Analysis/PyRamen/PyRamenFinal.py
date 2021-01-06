
#Import libraries
import csv
from pathlib import Path
#Set file paths for menu_data.csv and sales_data.csv
menu_path= Path('menu_data.csv')
sales_path= Path('sales_data.csv')
menu = []
#Read in the menu data into the menu list
with open(menu_path,'r') as menu_data:
    csvreader = csv.reader(menu_data, delimiter=',')
    csv_header = next(csvreader)
    for data in csv.reader(menu_data):
        menu.append(data)
sales = []
report = {}
#Read in the sales data into the sales list
with open(sales_path,'r') as sales_data:
    csvreader = csv.reader(sales_data, delimiter=',')
    csv_header = next(csvreader)
    for row in csv.reader(sales_data):
        sales.append(row)
# Initialize a row counter variable
row_count = 0
count = 0
revenue = 0.00
cogs = 0.00
net_profit = 0.00
#Logic and Looping time
for sale in sales:
    menu_item=sale[4]
    count=int(sale[3])
    row_count+=1
    if menu_item not in report.keys():
        report[menu_item] = {"count":count,}
    else: 
        report[menu_item]["count"] += count
for line in menu:
    item=line[0]   
    price=(float(line[3]))
    cost=(float(line[4]))
    if item in report.keys(): 
        report[item]["revenue"]= report[item]["count"]*price
        report[item]["cogs"]=report[item]["count"]*cost
        report[item]["net_profit"]=report[item]["count"]*(price-cost)
hw2="PyRamenOutput.txt"
output = (str(report).replace('}, ',',\n '))
with open(hw2,"w") as data:
    data.write(output)