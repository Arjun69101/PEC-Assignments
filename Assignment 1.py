#Assignment 1

#Question 1
#Find average of three numbers input by the user


#input your numbers
num1=input('Enter a number: ')
num2=input('Enter another number: ')
num3=input('Enter another number: ')

#sum of all inputs
s=int(num1)+int(num2)+int(num3)

#average of sums
avg=s/3

print('average:',avg)

#Question 2
#Compute a person's income tax


#input gross income
a=input('Enter your gross income in dollars: ')

#input number of dependents
b=input('Enter the number of dependents: ')

#Taxable income= gross income-$10000-(no. of dependants*$3000)
c=int(a)-10000-(3000*int(b))

#Tax=taxable income* tax rate(20%)
d=c*(20/100)

print('Income Tax:',d)


#Question 3
#Input student details


#input student name
Name=input('Enter your name: ')

#input SID
SID=input('Enter your student id: ')

#input gender
Gender=input('Enter your gender (M for male, F for female, U for unknown): ')

#input name of course
CourseName=input('Enter your course name: ')

#input your cgpa
CGPA=input('Enter your exact CGPA: ')

#all information in list form
student=[Name, SID, Gender, CourseName, CGPA]

print(student)


#Question 4
#Enter marks of 5 students


#list of marks
s1=input('marks of student 1: ')
s2=input('marks of student 2: ')
s3=input('marks of student 3: ')
s4=input('marks of student 4: ')
s5=input('marks of student 5: ')

x=[s1,s2,s3,s4,s5]

#sorting list in ascending order
x.sort()

print('List in ascending order: ',x)


#Question 5a
#Remove 4th element from list


#list of colours
colour_list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#removing black, the 4th element
colour_list.remove('Black')

print('colour',colour_list)


#Question 5b
#Remove black and pink from list and replace with purple


#list of colours
x=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#removing black and pink and replacing with purple
x.remove('Pink')
x[3]='Purple'

print(x)
