def fact(no):
    i=1
    fact=1
    while i<=no:
        fact=fact * i
        i=i+1
    print("factorial of ",no,' is ',fact)


num=int(input('Enter Number : '))
fact(num)