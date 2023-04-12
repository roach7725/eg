i=0 #initializing i
numyr=int(input("Enter the number of years ")) #asking for user input for the number for the years
k=1#declaring k's value
while(i<numyr):#using  a while loop with condition i is less than the number of years
    j=0#initializing j
    m=0#initializing m
    ttl=0#initializing total
    print(f"For year {k} :")#printing year number for desired output
    k+=1
    while(j<12):#using a while loop with condition j is less than 12
        m=int(input("Enter the rainfal for month"))
        print(f"Enter the rainfal amount  for month-",j+1,"",m)
        ttl=ttl+m#adding monthly rainfall to total which will initially be 0 and while increase every user inputs rainfall data
        j+= 1
    print("for",j+1,"months")#printing for the desired output
    print("Total rainfall",ttl,"","inches")#printing for the desired output
    avgrf=ttl/12#calculating average rainfall by diving total rainfall by 12
    print("Average rainfall",avgrf,"","inches")#printing for the desired output
    i=i+1#increasing i at the completion of loop



