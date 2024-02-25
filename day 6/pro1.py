#a shopping mall having 5 percent discount for men and 7 percent discount per women and individual discount for each item 3*no of item they purchase calculate the total bill
d={}
n=int(input("enter the no of items: "))
for i in range(n):
    k=input("enter item: ")
    v=int(input("enter item price: "))
    d[k]=v
l=[]
for i in d:
    l.append(d[i]-d[i]*(3*n)/100)
g=input("enter gender: ")
if g=="male":
    bill=sum(l)-sum(l)*5/100
else:
    bill=sum(l)-sum(l)*7/100
j=0
print("item-prices: discount-prices")
for i in d:
    print(f"{i}-{d[i]}:{l[j]}")
    j+=1
else:
    print("*"*12)
    print(f"total bill:{bill}")
