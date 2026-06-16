'''
                            #---------syntax of recursive
def func():
    if basecondition:
        return
    func()
                            #---------print no's 
def func(num):
    if num == 0:
        return
    print(num,end=' ') # reverse ex=> 5 4 3 2 1
    func(num-1)
func(5)

                            #---------print no's    
def func(num):
    if num == 0:
        return
    
    func(num-1)
    print(num,end=' ') # ex=> 1 2 3 4 5
func(5)


                            #---------sum of digits 
def sum_digits(n):
    if n == 0:
        return 0
    return n+sum_digits(n-1)
n=int(input("Enter the value: "))
print(sum_digits(n))

                            #---------power of digits  n^n

def power(bas,pow):
    if pow==0:
        return 1
    return bas * power(bas,pow-1)
print(power(2,4))
                            #---------power of digits  n^n user input
def power(bas,pow):
    if pow==0:
        return 1
    return bas * power(bas,pow-1)

bas = int(input())
pow = int(input())
print(power(bas,pow))

                            #---------Reverse_strings
def reverse_str(s,ind):
    if ind == 0:
        return s[0]
    return s[ind]+reverse_str(s,ind-1)
s = 'python programing'
print(reverse_str(s,len(s)-1))

'''

