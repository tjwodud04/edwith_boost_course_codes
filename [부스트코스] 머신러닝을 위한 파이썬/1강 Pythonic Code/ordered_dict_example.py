from collections import OrderedDict

d = {}
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

for k, v in d.items():
    print(k, v)
print()
'''
x 100
y 200
z 300
l 500
'''

d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

for k, v in d.items():
    print(k, v)
print()
'''
x 100
y 200
z 300
l 500
'''

for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[0])).items():
    print(k, v)
print()
'''
l 500
x 100
y 200
z 300
'''

for k, v in OrderedDict(sorted(d.items(),
                        reverse=True, key=lambda t: t[1])).items():
    print(k, v)
'''
l 500
z 300
y 200
x 100
'''