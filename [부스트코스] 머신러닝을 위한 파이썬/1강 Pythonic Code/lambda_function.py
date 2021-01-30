def f(x, y):
    return x + y

print(f(1, 4))
'''
5
'''

f = lambda x, y: x + y
print(f(1, 4))
'''
5
'''

f = lambda x: x ** 2
print(f(3))
'''
9
'''

f = lambda x: x / 2
print(f(3))
'''
1.5
'''

print((lambda x: x + 1)(5))
'''
6
'''
