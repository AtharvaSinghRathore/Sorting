import array as arr
x=arr.array('i')
requirement=int(input("How many number to sort: "))
y=range(requirement)
for i in y: x.append(int(input("Enter a number: ")))
for i in y:
 m=i
 j=0
 for j in range(i+1, requirement):
  if x[j]<x[m]:
   m=j
 x[i],x[m]=x[m],x[i]
for i in y: print(x[i])