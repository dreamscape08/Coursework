
#PyBank Homework2
#Jeffrey Scott
#import budget data and run an analysis of profit/loss and months they coincide with
#output file is HW2 
#%%
import csv
hw2 = 'PyBankOutput.txt'
csvpath = 'budget_data.csv'
with open(csvpath, 'r') as revenue_data:
    csvreader = csv.reader(revenue_data, delimiter = ",")
    csv_header = next(csvreader)    
   
    months = []
    profit = []
    profittotals = 0
    losstotals = 0 
    loss = []
    profits_loses = []
    
    for row in csv.reader(revenue_data):
        months.append(row[0])
        profits_loses.append(row[1])
    number_of_months=len(months)           
    
    for values in profits_loses:        
        if int(values) > 0:
            profit.append(values)
            profittotals= profittotals + int(values)
        elif int(values) < 0:
            loss.append(values)
            losstotals=losstotals+int(float(values))

    biggest_loss = 0 
    biggest_gain = 0
    for gain in profits_loses:
        if int(gain) > biggest_gain:
            biggest_gain = int(gain)
        elif int(gain) < biggest_loss:
            biggest_loss = int(gain)
    index_date_gain= profits_loses.index(str(biggest_gain))
    index_date_loss= profits_loses.index(str(biggest_loss))       
    revenue=(profittotals + losstotals)
    avg = revenue/number_of_months 

    output=(f'\nFinancial Analysis\n'
            f'-------------------------------------\n'    
            f'Total months invested: {number_of_months} months\n'
            f'Total years invested: {round(number_of_months/12,2)} years\n'
            f'# of profitable months: {len(profit)} months\n'
            f'# of unprofitable months: {len(loss)} months\n'
            f'-------------------------------------\n'
            f'Total sum of loses: ${losstotals}\n'
            f'Total sum of profits: ${profittotals}\n'
            f'Total revenue: ${(revenue - (losstotals*2))}\n'
            f'Total net profit: ${revenue}\n'
            f'-------------------------------------\n'
            f'Net Monthly Avg: ${round(avg,2)}\n'
            f'Net Weekly Avg: ${round(avg/4,2)}\n'
            f'Net Daily Avg: ${round(avg/28,2)}\n'
            f'-------------------------------------\n'
            f'Greatest Increase in Profits: {months[index_date_gain]} ${biggest_gain}\n'
            f'Greatest Decrease in Profits: {months[index_date_loss]} ${biggest_loss}\n')
    print(output)
    with open(hw2,"w") as data:
        data.write(output)


# %%




# %%
