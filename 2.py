a=input('Enter your gross income in dollars: ')
#input gross income
b=input('Enter the number of dependents: ')
#input number of dependents
c=int(a)-10000-(3000*int(b))
#Taxable income= gross income-$10000-(no. of dependants*$3000)
d=c*(20/100)
#Tax=taxable income* tax rate(20%)
print(d)