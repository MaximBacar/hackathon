import datetime
from datetime import timedelta
class moneyInfo:

    balance = 0 # balance as a float
    transactionList = [] # a list that will hold dictionaries of transaction
    subscriptionList = [] # a list that will hold dictionaries of monthly subscriptions
    salaryList = [] # a list that will hold dictionaries of salary   

    # parameterized constructor
    def __init__(self, b, tl, sl, s):
        self.balance = b
        self.transactionList = tl
        self.subscriptionList = sl
        self.salaryList = s

    # function to create a dictionary with price, name, date, and location
    # to be placed in the transaction list
    def transDict(servicePrice: float, clientName: str, purchaseDate: datetime, purchaseLocation: str, transList: list):
        
        dd1 = purchaseDate.strftime("%d %B %Y")
        dictionary1 = {"price" : servicePrice,
                      "name" : clientName,
                      "date" : dd1,
                      "location" : purchaseLocation} # dictionary

        transList.append(dictionary1) # append the dictionary to the list
        transList = sorted(transList, key=lambda d: d["date"]) # sort the list from oldest to newest year
        print(transList, "\n") # print the list for testing purposes
        return transList # return the list

     # function to create a dictionary with name, price, date, and pay periods
    # to be placed in the subscription list
    def subDict(serviceName: str, grossPrice: float, startDate: datetime, payPeriods: int, subList: list):
        
        dd2 = startDate.strftime("%d %B %Y")
        dictionary2 = {
                      "grossPrice" : grossPrice,
                      "serviceName" : serviceName,
                      "startDate" : dd2,
                      "payPeriods" : payPeriods} # dictionary

        subList.append(dictionary2) # append the dictionary to the list

        subList = sorted(subList, key=lambda d: d["startDate"]) # sort the list from oldest to newest year 
        
        print(subList, "\n") # print the list (for testing)
        dd3 = startDate + timedelta(days=payPeriods) # calculates and add the next payment from the last payment
        dd3 = dd3.strftime("%d %B %Y")
        print("The next payment day is", dd3, "\n") # prints next payment day
        return subList # return the list

    # function to create a dictionary with price, date and pay periods to be placed in the salary list
    def salaryDict(salaryPrice : float, startDate: datetime, periodDays : int, salDict : list):
        dd4 = startDate.strftime("%d %B %Y")
        dicitonary3 = {"salaryPrice" : salaryPrice,
                    "startDate" : dd4,
                    "periodDays" : periodDays
                     } # dictionary
        salDict.append(dicitonary3) # append the dicitonary to the list
        salDict = sorted(salDict, key=lambda d: d["startDate"]) # sort the list from oldest to newest year
        print(salDict, "\n") # print the list for testing purposes 
        dd5 = startDate + timedelta(days=periodDays) # calculates next income installment (next time the client gets paid)
        dd5 = dd5.strftime("%d %B %Y")
        print("The next income is", dd5, "\n") # prints the next payment day
        return salDict # returns the salary list

# outside the class, a function is created where it takes an object from the class as a parameter
# this function is incompleted but purpose is to calculate all expenses and income amount and compare them
# right now, the first part is completed, thus it shows the amount of money of every year and of every month of that year
def account(info : moneyInfo):

    # since there are two sources of payment, the latest year and the oldest year needs to be found
    year1 = info.transactionList[0]["date"] # get the oldest year of the transaction list
    year2 = info.subscriptionList[0]["startDate"] # get the oldest year of the subscription list
    year1 = int (year1[-4:]) # get the year as an int for the transaction list
    year2 = int (year2[-4:]) # get the year as an int for the subscription list

    year3 = info.transactionList[-1]["date"] # get the latest year of the transaction list
    year4 = info.subscriptionList[-1]["startDate"] # get the oldest year of the subscription list
    year3 = int (year3[-4:]) # get the year as an int for the transaction list
    year4 = int (year4[-4:]) # get the year as an int for the subscription list

    bigTotal = 0 # the big total of all expenses ever
    
    if year1 < year2: 
        year = year1 # if the year of the transaction list is older than the one from subscription list
                     # then that year is the reference year that will be used 
    else:
        year = year2

    if year3 > year4: 
        endYear = year3 # if the year of the transaction list is later than the one from subscription list
                        # then that year is the reference year that will be used 
    else:
        endYear = year4

    print(year) # print the reference year for oldest for testing purposes
    print(endYear) # print the reference year for latest for testing purposes


    while endYear >= year: # the while loop goes through all the years

        accountList1 = [] # list for the transaction dictionaries that share the same year
        accountList2 = [] # list for the subscription dictionaries that the same year
        boul2 = True # for the second while loop to loop through the months
        incr = 1 # for the value to go through the months dictionaries 

        # loop throughs the transaction list to find dictionaries with common years
        for y in range(len(info.transactionList)):
            if str(year) in info.transactionList[y]["date"]:
                print(info.transactionList[y])
                accountList1.append(info.transactionList[y])

        # loop throughs the subscription list to find dictionaries with common years                           
        for z in range(len(info.subscriptionList)):
            if str(year) in info.subscriptionList[z]["startDate"]:
                accountList2.append(info.subscriptionList[z])

        # second while loop to loop through the months to calculate the expenses of every month for a given year
        while boul2 == True:
            sameMonthList = [] # list for all the dictionaries with the same month and year
            month = {1: "January", 
                    2: "February", 
                    3: "March", 
                    4: "April", 
                    5: "May", 
                    6: "June", 
                    7: "July", 
                    8: "August", 
                    9: "September", 
                    10: "October", 
                    11: "November", 
                    12: "December"} # dictionary of months
               
            # loop through the year transaction list to find common months  
            for v in range(len(accountList1)):
                if month[incr] in accountList1[v]["date"]:
                    sameMonthList.append(accountList1[v])

            # loop through the year subscription list to find common months  
            for vv in range(len(accountList2)):
                if month[incr] in accountList2[vv]["startDate"]:
                    sameMonthList.append(accountList2[vv])

            # print all the new lists for testing purposes
            print(accountList1)
            print(accountList2)
            print(sameMonthList)

            total = 0 # total amount monthly

            # loops through the list of the expenses with the same month and year and adds up
            for u in range(len(sameMonthList)):
                if len(sameMonthList) != 0: 
                       
                    if "grossPrice" in sameMonthList[u]:
                        total = total + sameMonthList[u]["grossPrice"]
                        bigTotal = total +bigTotal
                    else:
                        total = total + sameMonthList[u]["price"]
                        bigTotal = total + bigTotal

            # prints message of total amount
            print("The total amount of your expenses on", month[incr], year, "are of ", total, "$")
            incr = incr+1 # increments to check the next month
            if incr == 13: # once all the months has passed, end the second while loop and go back to the other loop with the incremented year
                boul2 = False
                year = year +1

            # print the new year that is being checked, the last year, and the absolute total for testing purposes        
            print(year) 
            print(endYear)
            print(bigTotal)

    


# TESTING ALL THE METHODS HERE, ALL OF THESE ARE FAKE INFO FOR TESTING PURPOSES 
salaryList = []
subscriptionList = []
transactionList = []

infoooo = moneyInfo(1000, transactionList, subscriptionList, salaryList)

infoooo.transactionList = moneyInfo.transDict(38.99, "Loid", datetime.datetime(2021, 1, 11), "New Brunswick", transactionList)
infoooo.transactionList = moneyInfo.transDict(3.99, "John", datetime.datetime(2020, 12, 3), "Montreal", transactionList)

infoooo.subscriptionList = moneyInfo.subDict("Coffee Tim Hortons", 2.99, datetime.datetime(2020, 12, 22), 27, subscriptionList)
infoooo.subscriptionList = moneyInfo.subDict("ApplePay", 89.98, datetime.datetime(2019, 5, 14), 27, subscriptionList)

infoooo.salaryList = moneyInfo.salaryDict(673.78, datetime.datetime(2017, 2, 16), 14, salaryList)
infoooo.salaryList = moneyInfo.salaryDict(699.34, datetime.datetime(2016, 5, 2), 14, salaryList)

account(infoooo)