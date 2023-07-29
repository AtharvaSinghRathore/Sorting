import array as arr

x = arr.array('i')
requirement = int(input("How many numbers to sort: "))
r = range(requirement)

for i in r:
    x.append(int(input("Enter a number: ")))

lb = 0
ub = requirement
y = lb + 1
while y < ub:
    num = x[y]
    i = y - 1
    while i >= lb and x[i] > num:
        x[i + 1] = x[i]
        i = i - 1
    x[i + 1] = num
    y = y + 1

y = 0
while y < requirement:
    print(x[y])
    y = y + 1
