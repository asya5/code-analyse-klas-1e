#sets
A = {1,2,3,4,5}
type(A)

#empty set
A = set()

#dictionary
A = {}

#tuple
mytuple = (1,2,3,4'abd')
for i in mytuple:
  print(i)

x = 2
s = ''
while x > 0:
  y = 0
  while y < 4:
    s = s + str(x) + ':' + str(y) + ' '
    y = y + 1
  x = x - 1
print(s)
