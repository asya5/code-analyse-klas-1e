#does the user give an input to num?
#assignment analyse case 1 to 5 checked and correct

#CASE 1
num = 123456786

x = [int(a) for a in str(num)]

n = x.pop()

z = (sum(x))

if z%10== n:
    print('VALID')
else:
    print ('INVALID')

#CASE 2
num = 123456789

x = [int(a) for a in str(num)]

n = x.pop()

z = (sum(x))

if z%10== n:
    print('VALID')
else:
    print ('INVALID')

#CASE 3
num = 123

x = [int(a) for a in str(num)]

n = x.pop()

z = (sum(x))

if z%10== n:
    print('VALID')
else:
    print ('INVALID')

#CASE 4
num = 321

x = [int(a) for a in str(num)]

n = x.pop()

z = (sum(x))

if z%10== n:
    print('VALID')
else:
    print ('INVALID')

#CASE 5
num = 12

x = [int(a) for a in str(num)]

n = x.pop()

z = (sum(x))

if z%10== n:
    print('VALID')
else:
    print ('INVALID')
