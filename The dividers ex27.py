n=int(input("type the number"))
while n==0 :
    n=int(input("typr a non-zero number :"))
for i in range (1,n+1) :
    d=n%i
    if d==0 :
        print("the divider is :",i)
        