# Question 1
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
average=(num1+num2+num3)/3
print("The average of the three numbers is ",average)


# Question 2
grossincome=float(input("Enter the gross income to the nearest penny: "))
dependent=int(input("Enter number of dependents: "))
standard_deduction=10000
dependant_deduction=dependent*3000
taxable_income= grossincome-standard_deduction-dependant_deduction
tax=0.2*taxable_income #20% of the taxable income is the payable tax
print("Payable tax is: ",tax)

# Question 3
student_details=[]
SID=int(input("Enter SID: "))
name=str(input("Enter Name: "))
gender=str(input("Enter Gender: "))
course_name=str(input("Enter Course Name: "))
cgpa = float(input("Enter CGPA: "))
student_details.append(SID)
student_details.append(name)
student_details.append(gender)
student_details.append(course_name)
student_details.append(cgpa)
print("Student Details:", student_details)

# Question 4
studentmarks=[]
for i in range(5):
    print("Input marks",i+1," ")
    marks=int(input())
    studentmarks.append(marks)
studentmarks.sort()
print("Marks of students in ascending order are: ",studentmarks)

# Question 5
color=["Red","Green","White","Black","Pink","Yellow"]
color.remove("Black") #Removing black from the list
print("List after removing 'Black': ",color)
color=["Red","Green","White","Black","Pink","Yellow"]
color[3:5]=["Purple"] #Replacing Black and Pink with Purple
print("List after replacing 'Black' and 'Pink' with 'Purple' ",color)
