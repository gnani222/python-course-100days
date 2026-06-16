'''

def display():
    n=10
    print('Inside',n)
display()
print('Outside',n)

                        #------/n-------
n=10
def display():
    print('Inside',n)
display()
print('Outside',n)
                        #------/n-------string

def update(s):
    s += " Python"
    print("inside:", s)

s = "Hello"
update(s)
print("outside:", s)
                        #------/n-------integer

def update(n):
    n+=10
    print('inside:',n)

n=10
update(n)
print('outside',n)
                        #------/n-------float

def update(n):
    n+=10.5
    print('inside:',n)

n=10
update(n)
print('outside',n)
                        #------/n-------complex

def update(n):
    n+=10
    print('inside:',n)

n=13+4j
update(n)
print('outside',n)
                        #------/n-------list         

def update(n):
    n+=[1,8]
    print('inside:',n)

n=[1,2,3]
update(n)
print('outside',n)
                        #------/n-------tuple

def update(n):
    n+=(1,8)
    print('inside:',n)

n=(1,2,3)
update(n)
print('outside',n)
                        #------/n-------set

def update(n):
    n.add(4)
    print('inside:',n)

n={1,2,3}
update(n)
print('outside',n)

                        #------/n-------dictionary
def update(d):
    d['course']='python'
    print('inside:',d)

d={'name':'prakash'}
update(d)
print('outside',d)

'''                        #------/n-------bool

def update(n):
    n=False
    print('inside:',n)

n=True
update(n)
print('outside',n)



