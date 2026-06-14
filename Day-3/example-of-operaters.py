Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=10
a+b
30
a-b
10
a*
SyntaxError: invalid syntax
a*b
200
a/b
2.0
9/2
4.5
9//2
4
a**2
400
6**3
216
a%b
0
17%3
2
17%4
1
a
20
b
10
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
y=5
y
5
y=y+5
y
10
y=y+10
y
20
y+=10
y
30
y-=10
y
20
y*=4
y
80
y//=10
y
8
y%=2
y
0
y+=20
y
20
# logical0peraters
a
20
b
10
a%10==0
True
a%10==0 and b%20==0 a>b
SyntaxError: invalid syntax
a%10==0 and b%20==0 and a>b
False
a%10==0 or b%20==0 or a>b
True
a%10==0 or b%20==0 or a<b
True
a%22==0 or b%20==0 or a<b
False
not a>b
False
# Membership operaters
# str, list, tuple, set, dict
a = 'python programing'
a
'python programing'
'y' in a
True
'z' not in a
True
'r' not in a
False
l = ['java', 'python', 'mysql', 'c++', 'html']
'java' in l
True
'css' in l
False
t = ('java', 'python', 'mysql', 'c++', 'html')
'python' in t
True
'css' in t
False
# operation in set
t = {'java', 'python', 'mysql', 'c++', 'html'}
'java' in t
True
'css' in t
False
# operation in dict
d = {'sugar':20,'oil':110, 'paste':45}
45 in d
False
'paste' in d
True
'egg' in d
False
110 in d # its not defines without names
False
# identity operaters
l = [1,2,3,4,5]
m = [1,2,3,4,5]
l==m
True
n=m
n
[1, 2, 3, 4, 5]
n==m
True
l is n
False
n is m
True
id(l)
2617324922816
id(n)
2617323785600
n is not l
True
l is m
False
l is not m
True
# bitwise operators
8&4
0
8& 14
8
# and gate works on equal bits like 11--1, 00--1

>>> 8 | 7
15
>>> 5 |6
7
>>> 10^ 12
6
>>> ~12
-13
>>> ~11
-12
>>> 15<<2
60
>>> 10>>1
5
>>> # output foramting of print statments methods
>>> a= 12
>>> b= 10.24
>>> c = python
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    c = python
NameError: name 'python' is not defined
>>> c = 'python'
>>> c
'python'
>>> print(a,b,c)
12 10.24 python
>>> print("a=",a "b=",b "c=",c)
SyntaxError: invalid syntax
>>> print("a=",a ,"b=",b ,"c=",c)
a= 12 b= 10.24 c= python
>>> print("a=",a ,"b=",b ,"c=",c,sep='')
a=12b=10.24c=python
>>> print("a=",a ,"b=",b ,"c=",c,sep='',end=)
SyntaxError: expected argument value expression
>>> print("a=",a ,"b=",b ,"c=",c,sep='',end='')
a=12b=10.24c=python
>>> print(f'a= {a},'b= {b},'c= {c})
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print(f'a= {a}','b= {b}','c= {c}')
...       
a= 12 b= {b} c= {c}
>>> print(f'a= {a}'b= {b}' 'c= {c}')
...       
SyntaxError: unterminated string literal (detected at line 1)
