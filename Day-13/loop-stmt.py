# str list tuple set dict range()
"""
for var in seq:
    print(var)


s = 'pyton'
for ch in s:
    print(ch)

l = ['sugar','oil','eggs']
for item in l:
    print(item)


s= {'bike','laptop','cpu'}
for i in s:
    print(s)

for i in range(1,11):
    print(i)

for i in range(2,51):
    print(i)
    
for i in range(2,51,2):
    print(i)

for i in range(0,6,2):# we need must to write the stating value either 0 is default value 
    print(i)              # we need to apply value

l = 1,2,3,4,5,6,7,8
for l in range(len(l)):
    print(i)

s= 'python'
for i in range(len(s)):
    print(i,s[i])

l = [7,2,3,4,5,6,7,9,8,4,3]
for i in range(len(l)):
    print(i,l[i])

t = 7,2,3,4,5,6,7,9,8,4,3
for i in range(len(t)):
    print(i,t[i])

s = 'looping'
for i in enumerate(s):
    print(i[0],i[1])

l = [1,2,3,4,5,6,7,8]
for i in enumerate(l):
    print(i[0],i[1])
    print(type(l))

t = 1,2,3,4,5,6,7,8
for i in enumerate(t):
    print(i[0],i[1])

for i in range(11):
    if i == 5: # using for trminate the loop
        break
    print(i)

for i in range(11):
    if i == 5:
        continue # using for skip the value
    print(i)


for i in range(11): # using for empty output or skip the error
        pass

s = 'looping statements'
for ch in s:
    if ch in 'aeiouAEIOU':
        print(ch)

l = [68,34,21,32,43,54,54,31,3,2,1]
for i in l:
    if i %2 == 0:
        print(i)

d = {'lap':0,'mou':2,'key':4,'toys':5}
for i in d:
    print(i)

t = 1,2,3,4,5,6
for i in range(len(t)):
    print(i,t[i])
    print(i*t[i])
    
name = {'subbu','nani','ram','achyuth','vamsi'}
for i in name:
    print(i.upper())
