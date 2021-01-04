# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_path = Path('../02Python_Analysis/PyRamen/menu_data.csv')
sales_path = Path('../02Python_Analysis/PyRamen/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_path,'r') as menu_data:
    csvreader = csv.reader(menu_data, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        menu.append(row)
# @TODO: Read in the sales data into the sales list
with open(sales_path,'r') as sales_data:
    csvreader = csv.reader(sales_data, delimiter=',')
    csv_header=next(csvreader)
    for row in csvreader:
        sales.append(row[3])
        sales.append(row[4])
# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
    report = {}

# Initialize a row counter variable
    row_count = 0

# @TODO: Loop over every row in the sales list object
    for row in sales:
        sales_item=row[4]
        quantity=row[3]
    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
        if sales_item not in report:
            report['sales_item'] = sales_item
        row_count=+1
    

    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit

    # @TODO: For every row in our sales data, loop over the menu records to determine a match

        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables

        # @TODO: Calculate profit of each item in the menu data


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item

            # @TODO: Print out matching menu data

            # @TODO: Cumulatively add up the metrics for each item key

        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match

    # @TODO: Increment the row counter by 1

# @TODO: Print total number of records in sales data

# @TODO: Write out report to a text file (won't appear on the command line output)
