#Question 1
def Towerofhanoi(n,start,extra,final):
    if n>0:
        Towerofhanoi(n-1,start,final,extra)
        print("Transfer disk from",start,"to",final)
        Towerofhanoi(n-1,extra,start,final)
        
Towerofhanoi(3,"A","B","C")

# Question 2
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def ncr(n,r):
    x=fact(n)/(fact(n-r)*fact(r))
    return int(x)    

row=int(input("Enter the number of rows "))
i=1
while i<=row:
    print(" "*(row-i),end="")
    j=0
    while j<i:
        print(ncr(i-1,j)," ",end="")
        j+=1
    print("\n")
    i+=1

#Recursion
def pascal_triangle(n,j,k):
    if n==0:
        print(" "*(j-1),1,"\n")
        return pascal_triangle(n+1,j,k)
    elif n==k:
        print("Done!")
        n=-1
    else:
        print(" "*(j-n),end="")
        x=0
        while x<=n:
            print(ncr(n,x),"",end="")
            x+=1
        print("\n")
        if n==k:
            print("Done!")
            n=-2
        return pascal_triangle(n+1,j,k)
    
k=int(input("Enter the number of rows "))
n=k-k
j=k+k
pascal_triangle(n,j,k)

#Question 3
def fun(a,b):
    quotient=a//b
    remainder=a%b
    print("The quotient is ",quotient)
    print("The remainder is ",remainder)
    result=[quotient,remainder]
    return result

a=int(input("Please enter the first number "))
b=int(input("Please enter the second number "))
result=fun(a,b)
print(result)
print("Callable ",callable(fun))

#Part b
print("a is zero ",a==0)
print("b is zero ",b==0)
print("Quotient is zero ",result[0]==0)
print("Qemainder is zero ",result[1]==0)
if(a==0):
    print("a is zero")

#Part c
d=[4,5,6]
result=result+d
print(result)
list1=[]
for i in result:
    if i>4:
        list1.append(i)
print("The values greater than 4 are ",list1)

#Part d
aset=set(list1)
print(aset)

#Part e
immutable_set=frozenset(aset)
print("The required immutable set",immutable_set)

#Part f
max=0
for i in immutable_set:
    if i>max:
        max=i
print("The required max value is ",max)
print("The required hash value is ",hash(max))


#Question 4
class Student:
    def __init__(self,name,rollnum):
        self.name=name
        self.rollnum=rollnum
    def __del__(self):
        print("Destructor called, The object is destroyed.")

p1=Student("Raghav",15)
print(p1.name)
print(p1.rollnum)

#Question 5
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

p1=Employee("Mehak",40000)
p2=Employee("Ashok",50000)
p3=Employee("Viren",60000)

#Part a
p1.salary=70000
print("The updated salary of Mehak is ",p1.salary)
#Part b
del p1
print("The record of Viren has been successfully deleted ")

#Question 6
def anagram(word):
    if len(word)==1:
        return [word];
    partial_words=anagram(word[1:])
    char=word[0]
    result=[]
    for perm in partial_words:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:])
    return result        

george_word=input("Please give a word ")
possible_words=anagram(george_word)
barbie_word=input("Give a word ")
print("Possible Words are ",possible_words)
print("If Barbie's word lies in the list, then their friendship is real.")

if barbie_word in possible_words:
    print("Friendship is real.")
else:
    print("Friendship is fake.")