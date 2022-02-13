def count_char(string): #function for when only one word is entered
    counts=dict()
    for i in string:
        if i not in counts:
            counts[i]=1
        else:
            counts[i]+=1
    return counts

def count_words(lst): #function for when more than one words are entered
    counts=dict()
    for word in lst:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1    
    return counts

str=input("Enter a string ")
ls=str.split()
count=dict()
if len(ls)==1:
    print("The counts of the characters are ",count_char(str))
else:
    print("The counts of the words are ",count_words(ls))

# Question 2
dd=int(input("Enter the day of the month "))
mm=int(input("Enter the month "))
yyyy=int(input("Enter the year from 1800 to 2025 "))

def incorrect_date(): 
    print ("You have entered the incorrect date")

if dd>31 or dd<1 or mm>12 or mm<1 or yyyy<1800 or yyyy>2025: #boundary conditions for inputting date
    incorrect_date()
elif dd>30 and mm in [4,6,9,11]: #boundary condition for last day of months with 30 days
    incorrect_date()
elif dd>28 and mm==2 and yyyy%4!=0: #boundary condition for the last day of february in a non leap year
    incorrect_date()
elif dd>29 and mm==2 and yyyy%4==0: #boundary condition for the last day of february in a leap year
    incorrect_date()    
else:
    if mm in [1,3,5,7,8,10] and dd==31:#condition for last day of months with 31 days
       dd=1
       mm+=1
    elif mm in [4,6,9,11] and dd==30:#condition for last day of months with 30 days
       dd=1
       mm+=1
    elif mm==12 and dd==31:#condition for the last day of the year
       dd=1
       mm=1
       yyyy=yyyy+1
    elif yyyy%4==0 and mm==2 and dd==29:#condition for the last day of february in a leap year
       dd=1
       mm=3
    elif yyyy%4!=0 and mm==2 and dd==28:#condition for last day of february in a non leap year
       dd=1
       mm=3        
    else:#condition for when the day is the 1st or in the middle of the month
       dd=dd+1
    print("The next date is %d/%d/%d"%(dd,mm,yyyy))


# Question 3
list1=list()
list2=list()
flag='Y'
while flag=='Y':
    number=int(input("Enter a number "))
    numbersq=number**2
    list1.append(number)
    list2.append(numbersq)
    flag=input("Enter Y to enter more values and enter N to stop ").upper()
    if flag.upper()!='Y'and flag.upper()!='N':
        print("Invalid Input")
        print("Data you've entered so far is ",list(zip(list1,list2)))

    elif flag.upper()=='N':
        print (list(zip(list1,list2)))

# Question4
def printoutput(a,b): #function to print the output
    print ("Your grade is %s and %s performance"%(a,b))
grade=int(input("Enter the grade between 4 and 10 "))
if grade==10:
    lettergrade='A+'
    performance='Outstanding'
    printoutput(lettergrade,performance) #calling function to print output
elif grade==9:
    lettergrade='A'
    performance='Excellent'
    printoutput(lettergrade,performance)
elif grade==8:
    lettergrade='B+'
    performance='Very Good'
    printoutput(lettergrade,performance)
elif grade==7:
    lettergrade='B'
    performance='Good'
    printoutput(lettergrade,performance)
elif grade==6:
    lettergrade='C+'
    performance='Average'
    printoutput(lettergrade,performance)
elif grade==5:
    lettergrade='C'
    performance='Below average'
    printoutput(lettergrade,performance)
elif grade==4:
    lettergrade='D'
    performance='Poor'
    printoutput(lettergrade,performance)
else:
    print("Invalid Input")

# Question 5
for i in range(5): #loop for each row
    for j in range(i): #loop for printing spaces
        print(" ",end="")
    for j in range(2*(5-i)-1): #loop for printing Alphabets
        print(chr(65 + j),end="")
    print()

#Question 6
studentdata=dict()
flag="Y" 
while flag=='Y': 
    sid=int(input("Enter SID "))
    name=input("Enter name ")
    studentdata[sid]=name 
    flag=input("Enter Y to enter more data and N to stop ").upper()
    if flag.upper()!='Y' and flag.upper()!='N': #condition for invalid input
        print("Invalid input")
    elif flag.upper()=='N':
        print(studentdata)
        print()

#part b 
exstudentdata=dict()
list1=list() 
for (i,j) in studentdata.items():
    exstudentdata[j]=i #exchanging keys and values
    list1.append((j,i)) #making a list with the values of the exhanged dictionary
list1.sort() #sorting list by name (which is the key in the exchanged dictionary)
sortdictbyname=dict(list1) #making a dictionary out of the sorted list 
print("The dictionary sorted by name is")
print (sortdictbyname)
print()
#part c
list2=list()
for (i,j) in studentdata.items():
    list2.append((i,j)) #making list out of the dictionary(The key is SID)
list2.sort() #sorting the list
sortdictbysid=dict(list2) #making dictionary out of sorted dictionary
print("The dictionary sorted by SID is")
print(sortdictbysid)

#part d
search=int(input("Enter the SID you want to search")) #searching for the SID (key)
if search in studentdata: 
    print("Found!")
    print("The student whose SID you have entered is",studentdata[search])
else:
    print("Sorry, the SID you have searched is not in the dictionary")



#Question 7
n1=0
n2=1
count=0
sum=0
nterms=int(input("Please enter the number of terms you want to print "))
if nterms <= 0: #checking that the input value is positive
   print("Please enter a positive integer ")
elif nterms == 1: #in case the input value is 1 
   print("Fibonacci series upto",nterms,":")
   print(n1)
else:
   while count < nterms: 
       sum+=n1 #summing values as we go along the loop
       print(n1,end=" ") 
       n3 = n1 + n2 #adding and exchanging values
       n1 = n2
       n2 = n3
       count += 1
       
average=sum/nterms
print()
print("The average of the terms of the fibonacci sequence is %f"%(average))


#Question 8
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

ansa=set1^set2 #set of all elements that are in Set1 and Set2 but not both
print(ansa)
ansb=set1^(set2^set3) #set of all elements that are in only one of the three sets
print(ansb)
ansc=(set1&set2)|(set2&set3)|(set1&set3) #set of elements that are in exactly two of the sets
print(ansc)
set4={1,2,3,4,5,6,7,8,9,10}
ansd=set4-set1 #set of all integers in the range 1 to 10 that are not in Set1
print(ansd)
anse=set4-(set1|set2|set3) #set of all integers in the range 1 to 10 that are not in set 1, 2, and 3
print(anse)
