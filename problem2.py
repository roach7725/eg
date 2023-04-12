ini_org=int(input("Enter the total number of organisms : "))#asking user input for initial organisms
daily_inc=int(input("Enter the daily increase : "))#asking user input for daily increase rate
days=int(input("Enter the number of days for the final result : "))#asking user input for days for final data
print("Starting number of organisms : ",ini_org)#printing population of initial organisms
print("Average daily  percentage increase : ",daily_inc)#prinitng the average increase rate
print("Enter the number of days for the final data : ",days)#printing the user input of days for final data
print("Day approximate","      ","population") #printing according to asked output                      
print("---------------------------------")#printing according to asked output 
for i in range(1,days+1):#using for loop it will run till days given by user starting from 1
    print(i,"                          ",ini_org)#printing according to asked output
    ini_org=ini_org+(ini_org*(daily_inc/100))#calculating the daily increase 
    