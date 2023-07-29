import array as arr
x=arr.array('i')
requirement=int(input("How many numbers to sort?: "))
y=range(requirement)
for i in y:x.append(int(input("Enter a number: ")))
j=range(requirement-1,0,-1)
for m in j:
	k=range(m)
	for e in k:
		if x[e+1]<x[e]:
			x[e],x[e+1]=x[e+1],x[e]
for i in y: print(x[i])


