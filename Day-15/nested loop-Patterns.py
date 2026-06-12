'''
s ='python'
for i in range(len(s)):
    for j in range(i+1, len(s)):
        print(s[i],s[j],sep='',end=' ')

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = sum(sum(row) for row in l) # to print sum of lists
print(total)


l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # nested list
total = 0
for i in l:  # using the nested loop to sum
    for j in i:
        total += j  # sum of nested list condition
print(f'total = {total}')


d = {
    '1234':{'pin':'4561','balance':2301},
    '1235':{'pin':'4562','balance':2302},
    '1236':{'pin':'4563','balance':2303},
    '1237':{'pin':'4564','balance':2304}
    }
for i in d:
    print('Account number: ',i)
    print('Pin number: ',d[i]['pin'])
    print('balance: ',d[i]['balance'])

for i in range(5):
    for j in range(5):
        print(i,end=" ")
    print()

n = int(input('Enter the Number: ')
for i in range(n):
        for j in range(n):
        print(j%2,end=' ')
    print()

n = int(input('Enter the Number: '))
for i in range(n):
        for j in range(n):
            print(j%2,end=' ')
        print()

for i in range(5):
    for j in range(5):
        if i >= j:
            print('*',end=" ")
    print()

n = int(input('Enter the Number: '))  
for i in range(n):
    for j in range(n-i):
        print('*',end=" ")
    print()


n = int(input('Enter the Number: ')) 
for i in range(n):
    for j in range(n):
        if i >= j:
            print(' ',end=" ")
        else:
            print('*',end=' ')
    print()

    
n = int(input('Enter the Number: '))
for i in range(n):
    for sp in range(n-1-i):
            print(' ',end=" ")
    for j in range(i+1):
            print('*',end=' ')
    print()


n = int(input('Enter the Number: '))
for i in range(n):
    for sp in range(i):
            print(' ',end=" ")
    for j in range(n-i):
            print('*',end=' ')
    print()

n = int(input('Enter the Number: '))
for i in range(n):
    for sp in range(i):
            print(' ',end=" ")
    for j in range(n-i):
            print('*',end=' ')
    print()

n = int(input('Enter the Number: '))
for i in range(n):
    for j in range(n):
        print((i+j)%2,end=' ')
    print()

a = int(input('Enter the Number: '))
b = 1
for i in range(n):
    for j in range(i+1):
        print(str(b),end=' ')
        b+=1
    print()
'''
