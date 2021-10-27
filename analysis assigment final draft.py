#analysis assignment case 1 to 5 checked and correct

#CASE 1

number = 123456786

d = [int(d) for d in str(number)]
print (d)
n = d.pop()

z = (sum(d))
print (sum(d))

if z%10==n:
    print('VALID')
else:
    print('INVALID')


#CASE 2

number = 123456789

d = [int(d) for d in str(number)]

n = d.pop()

z = (sum(d))

if z%10==n:
    print('VALID')
else:
    print('INVALID')

#CASE 3

number = 123

d = [int(d) for d in str(number)]

n = d.pop()

z = (sum(d))

if z%10==n:
    print('VALID')
else:
    print('INVALID')

#CASE 4

number = 321

d = [int(d) for d in str(number)]

n = d.pop()

z = (sum(d))

if z%10==n:
    print('VALID')
else:
    print('INVALID')

#CASE 5

number = 12

d = [int(d) for d in str(number)]

n = d.pop()

z = (sum(d))

if z%10==n:
    print('VALID')
else:
    print('INVALID')
