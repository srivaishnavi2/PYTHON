#write a python program to check the number is perfect or not
n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("prefect")
else:
    print("not a prefect")
