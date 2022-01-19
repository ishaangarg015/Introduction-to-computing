# Question 1

string1="Python is a case sensitive language"
print("Length of the string is", len(string1))
reverse_string1=string1 [::-1]
print(reverse_string1)
string2=string1[10:26] #Using slice function to store a substring in another variable
print(string2)
string3=string1[:10]+"object oriented"+string1[26:] #Creating a new string and replacing 'a case sensitive' by 'object oriented'
print(string3)
index=string1.find("a") #finding index of substring "a" in input dtring
print("index of a is",index)
string4=string1.replace(" ", "") #Removing whitespaces from the input string
print(string4)


# Question 2 
name=input("Enter your name ")
SID=input("Enter your SID ")
department=input("Enter your department name ")
CGPA=input("Enter your CGPA ")
print("Hey,",name,"Here!")
print("My SID is",SID)
print("I am from",department,"department and my CGPA is",CGPA)


# Question 3
a=56
b=10
print("Value of a&b is",a&b)
print("Value of a|b is",a|b)
print("Value of a^b is",a^b)
print("Value of 'a' after 2 bit left shift is",a<<2)
print("Value of 'b' after 2 bit left shift is",b<<2)
print("Value of 'a' after 2 bit right shift is",a>>2)
print("Value of 'b' after 4 bit right shift is",b>>4)

# Question 4
num1=int(input("Enter a number "))
num2=int(input("Enter the second number "))
num3=int(input("Enter the third number "))
if (num1>=num2) and (num1>=num3):
    greatest=num1
elif (num2>=num1) and (num2>=num3):
    greatest=num2
else:
    greatest=num3
print("The greatest number of the entered numbers is",greatest)

# Question 5
string=input("Enter a string ")
index=string.find(" name ")
if index==-1:
    print("NO")
else:
    print("YES")

# Question 6
side1=int(input("Enter the length of the first side "))
side2=int(input("Enter the length of the second side "))
side3=int(input("Enter the length of the third side "))
if side1+side2<=side3:
    print("No")
elif side1+side3<=side2:
    print("No")
elif side2+side3<=side1:
    print("No")
else:
    print("Yes")