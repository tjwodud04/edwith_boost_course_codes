# Map
def f(x, y):
    return x + y
print(f(1, 4))
'''
5
'''

f = lambda x,y: x+y
print(f(1, 4))
'''
5
'''

ex = [1, 2, 3, 4, 5]
f = lambda x: x ** 2
print(list(map(f, ex)))
'''
[1, 4, 9, 16, 25]
'''

ex = [1, 2, 3, 4, 5]
f = lambda x, y: x + y
print(list(map(f, ex, ex)))
'''
[2, 4, 6, 8, 10]
'''

list(map(lambda x: x ** 2 if x % 2 == 0 else x, ex))

ex = [1,2,3,4,5]
print(list(map(lambda x: x+x, ex)))
print((map(lambda x: x+x, ex)))
'''
[2, 4, 6, 8, 10]
<map object at 0x000001F72EC2E548>
'''

f = lambda x: x ** 2
print(map(f, ex))
'''
<map object at 0x000001B436A6EE08>
'''

for i in map(f, ex):
    print(i)
'''
1
4
9
16
25
'''

result = map(f, ex)
print(result)
print(next(result))
print()
'''
<map object at 0x000001B436A6EE08>
1
'''

import sys

sys.getsizeof(ex)
sys.getsizeof((map(lambda x: x+x, ex)))
sys.getsizeof(list(map(lambda x: x+x, ex)))

# Reduce
from functools import reduce

print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
'''
15
'''

def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))

print(factorial(5))
'''
120
'''