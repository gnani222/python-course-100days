'''
i = 1
while i<=11: # to print 1-11 numbers
    print(i)
    i+=1

i = 10
while i>0:
    print(i) # to print reverse in 0-10 no's
    i-=1

i = 2

l = [1,2,3,4,5,6,7]
i = 0
while i<len(l):
    print(l[i])
    i+=1

 
l = 'python'
i = 0
while i<len(l):
    print(l[i])
    i+=1



l = (1,2,3,4,5,6,7)
i = 0
while i<len(l):
    print(l[i])
    i+=1

l = [1,0,0,0,0,0,3,0,0,0,0,0,4,0,5]
i = 1
while 0 in l:
    l.remove(0)
print(l)

i = 10
while i >0 :
     # to print reverse in 0-10 no's
    i-=1
    print(i)

'''
m=10
while m>0:
    s= input(f"[W]in or [C]ontinue: ").upper()
    if s == 'W':
        print('you are win')
        break
    m-=1
    print(f'{m} moves left')
else:
    print("Game Over")
