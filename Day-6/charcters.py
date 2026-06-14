"""
s = input()
print("Total charaecters:",len(s))
print('First charecter :',s[0])
print('Last charecter :',s[-1])
print('Uppercase :',s.upper())
print('Reversed String :',s[::-1])
"""
#You are given the marks of N students across X subjects.
#Each of the next X lines contains N space-separated values, 
#representing marks scored by all students in one subject.
#Your task is to compute the average marks of each student. 
#Input Format : First line: Two integers N X Next X lines: Each line contains N space-separated marks. 
#Output Format : Print N lines, each containing the average marks of one student (up to 1 decimal place).

n, x = map(int, input().split())
m = []
for _ in range(x):
  m.append(list(map(float,input().split())))

for student in zip(*m):
  avg = sum(student)/x
  print(f"{avg:.1f}")