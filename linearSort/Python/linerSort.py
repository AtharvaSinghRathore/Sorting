import array as arr
x=arr.array('i')
y=range(5)
for i in y:x.append(int(input("Enter a number: ")))

k=range(4)
for e in k:
	j=range(e+1,5)
	for f in j:
		if x[f]<x[e]:x[e],x[f]=x[f],x[e]
for i in y: print(x[i])

