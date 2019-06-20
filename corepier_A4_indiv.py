#Corey Pierce
#I211 Homework 4

#1

'''
To display the full name of the day of the week, use "%A"
'''

#2

'''
Import csv and datetime module

set a variable to open the csv file

for every individual cell in data:

    set a variable to the item in the second index and split it with "/"

    Try:
        appending the first index in the cell to the varibale you chose from the step before

        set a variable week_day to the module datetime then getting full name of the weekday

        if the week_day equals saturday or sunday:

            print the 3rd index attached to your first variable.

        if not:

            pass



'''









#import csv and datetime

import csv, datetime

data = csv.reader(open("ShopRecords.csv", "r"))

for item in data:

    item_list = item[2].split("/")

    try:

        item_list.append(item[1])

        week_day = datetime.date(int(item_list[2]), int(item_list[0]),
                                 int(item_list[1])).strftime("%A")

        if week_day == "Saturday" or week_day == "Sunday":
            print(item_list[3])

    except:

        pass
