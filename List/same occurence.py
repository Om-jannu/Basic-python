def countOccurrences(arr, n, x):
    res = 0
    for i in range(n):
        if x == arr[i]:
            pos.append(i)
            res=res+ 1
        else:
            pass
    return res

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
pos=[]
print(arr)
n = len(arr)
x = int(input('Enter No to be searched : '))
print(x,' is found ',countOccurrences(arr, n, x),' times .')
print(x,' occurs at position ',pos)
