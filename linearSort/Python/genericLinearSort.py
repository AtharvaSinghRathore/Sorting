import array as arr
requirement=int(input("How many number to sort?: "))
x=arr.array('i')
y=range(requirement)
for i in y: x.append(int(input("Enter a number: ")))
k=range(requirement-1)
for e in k:
	j=range(e+1,requirement)
	for f in j:
		if x[f]<x[e]:x[e],x[f]=x[f],x[e]
for i in y: print(x[i])


