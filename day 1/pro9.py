#write a python program to check whether year is a leap year or not#
year=int(input())
if year%4==0 and year%100!=0:
    print("leap year")
else:
    print("not a leap year")
    
