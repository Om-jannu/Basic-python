list =[2,5,23,6,46,34,25]
a=[]
ch=0
print("unsorted list:")
print(list)
while ch!=3:
    ch = int(input('1.Ascending  2.Descending  3.Exit \n'))
    if ch==1:
        list.sort(reverse=False)
        print('Ascending Sorted list : ',list)

    elif ch ==2:
        list.sort(reverse=True)
        print('Desccending Sorted list : ',list)
    else:
        ch = 3

