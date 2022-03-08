# Question 1
from tkinter import*

def gst():
    originalcost=int(en1.get())
    netcost=int(en2.get())
    gst=((netcost-originalcost)*100)/originalcost
    en3.insert(12,str(gst)+"%")
def clear():
    en1.delete(0,END)
    en2.delete(0,END)
    en3.delete(0,END)    

win=Tk()
win.title("GST Calculator")
win.geometry("300x150")
lbl1=Label(win,text="Enter Original Price",font=("Arial",12))
lbl2=Label(win,text="Enter Net Price",font=("Arial",12))
lbl3=Label(win,text="GST is ",font=("Arial",12))
lbl1.grid(row=1,column=1)
lbl2.grid(row=2,column=1)
lbl3.grid(row=5,column=1)
en1=Entry()
en2=Entry()
en3=Entry()
en1.grid(row=1,column=2)
en2.grid(row=2,column=2)
en3.grid(row=5,column=2)
but1=Button(win,text="Calculate GST",activebackground="light blue",relief=RIDGE,command=gst)
but2=Button(win,text="Clear",activebackground="light blue",relief=RIDGE,command=clear)
but1.grid(row=3,column=2)
but2.grid(row=6,column=2)
win.mainloop()

# Question 2
from tkinter import *
import calendar
def showCalender():
    gui=Tk()
    gui.title("Calender for the year")
    gui.geometry("600x600")
    year=int(year_field.get())
    gui_content=calendar.calendar(year)
    calYear=Label(gui,text= gui_content,font=("arial", 10,))
    calYear.grid(row=5, column=1,padx=10)
    gui.mainloop()
if __name__=='__main__':
    new=Tk()
    new.title("Calender For Any Year")
    new.geometry("300x200")
    year=Label(new, text="Enter year",font=("arial",12, "bold",))
    year_field=Entry(new,font=("arial",12,"bold",))
    button=Button(new,text='Show Calender',command=showCalender,font=("arial",12,"bold",))
    Exit=Button(new,text="Exit",command=new.destroy,font=("arial",12, "bold",))
    year.grid(row=2,column=1)
    year_field.grid(row=3,column=1)
    button.grid(row=4,column=1)
    Exit.grid(row=5,column=1)
    new.mainloop()

# Question 3
from tkinter import*

def buttonclick(number):
    current=en1.get()
    en1.delete(0,END)
    en1.insert(0, str(current)+str(number))
def clearfun():
    en1.delete(0,END)    
def buttonadd():
    firstnum=en1.get()
    global f_num
    global sign
    sign="add"
    f_num=int(firstnum)
    en1.delete(0,END)
def buttonequal():
    secondnum=en1.get()
    en1.delete(0,END)
    if sign=="add":
       en1.insert(0,f_num+int(secondnum))
    if sign=="subtract":
       en1.insert(0,f_num-int(secondnum))
    if sign=="multiply":
       en1.insert(0,f_num*int(secondnum))
    if sign=="divide":
       en1.insert(0,f_num/int(secondnum))         
def buttonsubtract():
    firstnum=en1.get()
    global f_num
    global sign
    sign="subtract"
    f_num=int(firstnum)
    en1.delete(0,END)
def buttondivide():
    firstnum=en1.get()
    global f_num
    global sign
    sign="divide"
    f_num=int(firstnum)
    en1.delete(0,END)
def buttonmultiply():
    firstnum=en1.get()
    global f_num
    global sign
    sign="multiply"
    f_num=int(firstnum)
    en1.delete(0,END)

win=Tk()
win.title("Calculator")
win.geometry("450x300")
#creating buttons
but1=Button(win,text="1",activebackground="light green",relief=GROOVE,padx=40,pady=20,command=lambda: buttonclick(1))
but2=Button(win,text="2",activebackground="light green",relief=GROOVE,padx=40,pady=20,command=lambda: buttonclick(2))
but3=Button(win,text="3",activebackground="light green",relief=GROOVE,padx=40,pady=20,command=lambda: buttonclick(3))
but4=Button(win,text="4",activebackground="light green",relief=GROOVE,padx=40,pady=20,command=lambda: buttonclick(4))
but5=Button(win,text="5",activebackground="light green",relief=GROOVE,padx=40,pady=20,command=lambda: buttonclick(5))
but6=Button(win,text="6",activebackground="light green",relief=GROOVE,padx=40,pady=20,command=lambda: buttonclick(6))
but7=Button(win,text="7",activebackground="light green",relief=GROOVE,padx=40,pady=20,command=lambda: buttonclick(7))
but8=Button(win,text="8",activebackground="light green",relief=GROOVE,padx=40,pady=20,command=lambda: buttonclick(8))
but9=Button(win,text="9",activebackground="light green",relief=GROOVE,padx=40,pady=20,command=lambda: buttonclick(9))
but0=Button(win,text="0",activebackground="light green",relief=GROOVE,padx=40,pady=20,command=lambda: buttonclick(0))
butplus=Button(win,text="+",activebackground="light green",relief=GROOVE,padx=40,pady=20,command=buttonadd)
butminus=Button(win,text="-",activebackground="light green",relief=GROOVE,padx=40,pady=20,command=buttonsubtract)
butmult=Button(win,text="*",activebackground="light green",relief=GROOVE,padx=40,pady=20,command=buttonmultiply)
butdiv=Button(win,text="/",activebackground="light green",relief=GROOVE,padx=40,pady=20,command=buttondivide)
buteq=Button(win,text="=",activebackground="light green",relief=GROOVE,padx=40,pady=20,command=buttonequal)
butclear=Button(win,text="C",activebackground="light green",relief=GROOVE,padx=40,pady=20,command=clearfun)
#creating entry box
en1=Entry()
#placing entry box and buttons
en1.grid(row=1,column=1,columnspan=4)
but1.grid(row=2,column=1)
but2.grid(row=2,column=2)
but3.grid(row=2,column=3)
but4.grid(row=3,column=1)
but5.grid(row=3,column=2)
but6.grid(row=3,column=3)
but7.grid(row=4,column=1)
but8.grid(row=4,column=2)
but9.grid(row=4,column=3)
but0.grid(row=5,column=2)
butplus.grid(row=2,column=4)
butminus.grid(row=3,column=4)
butmult.grid(row=4,column=4)
butdiv.grid(row=5,column=4)
butclear.grid(row=5,column=1)
buteq.grid(row=5,column=3)
win.mainloop()

# Question 4
def quicksort(arr,left,right):
   if left<right:
        partition_pos=partition(arr,left,right)
        quicksort(arr,left,partition_pos-1)
        quicksort(arr,partition_pos+1,right)
def partition(arr,left,right):
    i=left
    j=right-1
    pivot=arr[right]
       
    while i<j:
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
         arr[i],arr[right]=arr[right],arr[i]
    return i



num=int(input("Enter the number of students whose marks you have to enter "))
li=list()
for i in range(num):
    n=int(input("Enter marks "))
    li.append(n)     
print("The list you have entered is ",li)
quicksort(li,0,num-1)
print("Sorted list is: ",li)

#Question 5
n=int(input("Enter the number of elements you want your list to be "))
li=list()
for i in range(n):
    element=int(input("Enter the element of the list "))
    li.append(element)
print("The entered list is ",li)
li.sort()
print("Sorted list is ",li)

#part b
def binarySearch(array,x,low,high):
    # Repeat until the pointers low and high meet each other
    while low<=high:
        mid=low+(high-low)//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
search=int(input("Enter the number you want to search for "))
result=binarySearch(li,search,0,n-1)
if result!=-1:
    print("Element is present at index "+str(result))
else:
    print("Not found")

#part c
count=0
if result!=-1:
    for number in li:
        if number==search:
            count+=1
print("The number you are looking for occurs %d times"%(count))            