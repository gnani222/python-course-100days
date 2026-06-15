
def function_name(arg):
    #statments

def wish(name):
    print(f"Welcome to the python!")
wish(nani)
wish(anu)
wish(ram)
wish(jai)

def iseven(num):
    if num%2==0:             # stmt for finding even no's---/n----
        return f"{num} - Even Number"
    else:
        return f" {num} - Odd Number"
print(iseven(12))
print(iseven(13))

def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact*=i                # stmt for find factorial ---/n----
    return fact
num = int(input("Enter The Number: "))
print("Factorial:" , factorial(num))

def isprime(num):
    for i in range(2,num//2):
        if num%2==0:           # stmt for finding prime no's---/n----
            return f"{num} - Not a prime Number"
    
    return f" {num} - prime Number"
num = int(input("Enter the number: "))
print(isprime(num))


                            # positional Arguments:---/n----

def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Passwoerd:",pwd)
display('nani','nani1234@gamail.com','Nani#2003')
display('nani','nani$1234','Nani2003@gmail.com')
display('nani@gmail.com','nani@1234','Nani#2003')

                            # Key word arguments:---/n----

def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)
display(name='nani',email='nani1234@gamail.com',pwd='Nani#2003')
display(name='nani',pwd='nani$1234',email='Nani2003@gmail.com')
display(email='nani@gmail.com',name='nani',pwd='Nani#2003')



                            # default Arguments:---/n----
'default value start with on last parameter'
def display(name,email,pwd=' '):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)
display(name='nani',email='nani1234@gamail.com',pwd='Nani#2003')
display(name='nani',pwd='nani$1234',email='Nani2003@gmail.com')
display(email='nani@gmail.com',name='nani')



                             # possitional variables:---/n----
def display(*names):
    print("Names:",names)

display('nani','mani','ani')
display('nani','mani','anu')
display('nani','ani')
display('nani','mani')
                            # keyword varaibles:---/n----
def display(*names):
    print("Names:",names)

display(k='nani',k1='mani',k2='anu')
display(k='nani',k1='mani')
