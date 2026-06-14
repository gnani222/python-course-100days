'''
correct_password = "Nani"
attempts = 3

for attempt in range(attempts):
    password = input("Enter password: ")

    if password == correct_password:
        print("Phone Unlocked")
        break
    else:
        remaining = attempts - attempt - 1
        print("Inncorect pin")

else:
    raise Exception("Too many failed attempts! Access denied.")


l = [1,2,3,4,5,6,7,8,9]
s = int(input())
for i in range(len(l)):
    if l[i] == s:
        print(f"{l[i]}Number is found at index-[i] ")
        break
else:
    print("not found")

p = input()
if len(p)>=8:
    s=set()
    for i in p:
        if i.islower():
            s.add('u')
        elif i.isupper():
            s.add('l')
        elif i.isdigit():
            s.add('d')
        else:
            s.add('s')
    if len(s)==4:
        print("strong")
    else:
        print("weak")
else:
    print("weak")
  

status  = True
assert status != None, 'hi hello'
print(status)

'''
