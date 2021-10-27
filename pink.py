num = 123456786
x = [int(a) for a in str(num)]
print(x)

n = x.pop()
print (n)

z = (sum(x))

if z%10== n:
    print('VALID')
else:
    print ('INVALID')


