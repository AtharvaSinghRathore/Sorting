import array as arr
x=arr.array('i')
requirement=int(input("How many numbers to sort: "))
y=range(requirement)
for i in y:x.append(int(input("Enter a number: ")))
lb=0
ub=requirement-1
e=lb
stk=[]
stk.append((lb,ub))
while len(stk)>0:
 (lb,ub)=stk.pop()
 e=lb
 f=ub
 while e<f:
  while e<ub and x[e]<=x[lb]: e=e+1
  while x[f]>x[lb]: f=f-1
  if e<f: x[e],x[f]=x[f],x[e]
  else: x[lb],x[f]=x[f],x[lb]
 pp=f
 if pp+1<ub: stk.append((pp+1,ub))
 if lb<pp-1: stk.append((lb,pp-1))
for i in y: print(x[i])

