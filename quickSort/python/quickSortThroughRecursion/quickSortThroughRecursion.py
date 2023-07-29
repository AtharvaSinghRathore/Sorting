import array as arr

def getPartitionPoint(x,lb,ub):
 e=lb
 f=ub
 while e<f:
  while e<ub and x[e]<=x[lb]: e=e+1
  while x[f]>x[lb]: f=f-1
  if e<f: x[e],x[f]=x[f],x[e]
  else: x[f],x[lb]=x[lb],x[f]
 return f

def quickSort(x,lb,ub):
 if lb>=ub: return
 pp=getPartitionPoint(x,lb,ub)
 quickSort(x,lb,pp-1)
 quickSort(x,pp+1,ub)
x=arr.array('i')
requirement = int(input("How many numbers to sort: "))
r = range(requirement)

for i in r: x.append(int(input("Enter a number: ")))

quickSort(x, 0, requirement - 1)

y = 0
while y < requirement:
 print(x[y])
 y = y + 1