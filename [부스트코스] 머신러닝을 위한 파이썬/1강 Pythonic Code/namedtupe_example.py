from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p[0] + p[1])
'''
33
'''

x, y = p
print(x, y)
print(p.x + p.y)
print(Point(x=11, y=22))
'''
11 22
33
Point(x=11, y=22)
'''

from collections import namedtuple
import csv

f = open("users.csv", "r")
print(next(f))
'''
user_id,integration_id,login_id,password,first_name,last_name,full_name,sortable_name,short_name,email,status
'''

reader = csv.reader(f)
student_list = []

for row in reader:
    student_list.append(row)
    print(row)
'''
['1555551', '', 'lrice', '', 'Lonnie', 'Rice', 'Lonnie Rice', 'Rice, Lonnie', 'Lonnie Rice', 'lrice@institution-name.edu', 'active']
['1555552', '', 'jthompson', '', 'Jan', 'Thompson', 'Jan Thompson', 'Thompson, Jan', 'Jan Thompson', 'jthompson@institution-name.edu', 'active']
['1555553', '', 'rreeves', '', 'Roger', 'Reeves', 'Roger Reeves', 'Reeves, Roger', 'Roger Reeves', 'rreeves@institution-name.edu', 'active']
['1555554', '', 'wgriffin', '', 'Warren', 'Griffin', 'Warren Griffin', 'Griffin, Warren', 'Warren Griffin', 'wgriffin@institution-name.edu', 'active']
['1555555', '', 'tsanders', '', 'Tammy', 'Sanders', 'Tammy Sanders', 'Sanders, Tammy', 'Tammy Sanders', 'tsanders@institution-name.edu', 'active']
['1555556', '', 'cprice', '', 'Carrie', 'Price', 'Carrie Price', 'Price, Carrie', 'Carrie Price', 'cprice@institution-name.edu', 'active']
['1555557', '', 'abowers', '', 'Alicia', 'Bowers', 'Alicia Bowers', 'Bowers, Alicia', 'Alicia Bowers', 'abowers@institution-name.edu', 'active']
['1555558', '', 'eramsey', '', 'Essie', 'Ramsey', 'Essie Ramsey', 'Ramsey, Essie', 'Essie Ramsey', 'eramsey@institution-name.edu', 'active']
['1555559', '', 'lwillis', '', 'Lila', 'Willis', 'Lila Willis', 'Willis, Lila', 'Lila Willis', 'lwillis@institution-name.edu', 'active']
['1555560', '', 'csoto', '', 'Corey', 'Soto', 'Corey Soto', 'Soto, Corey', 'Corey Soto', 'csoto@institution-name.edu', 'active']
'''

print(student_list)
'''
[['1555551', '', 'lrice', '', 'Lonnie', 'Rice', 'Lonnie Rice', 'Rice, Lonnie', 'Lonnie Rice', 'lrice@institution-name.edu', 'active'], ['1555552', '', 'jthompson', '', 'Jan', 'Thompson', 'Jan Thompson', 'Thompson, Jan', 'Jan Thompson', 'jthompson@institution-name.edu', 'active'], ['1555553', '', 'rreeves', '', 'Roger', 'Reeves', 'Roger Reeves', 'Reeves, Roger', 'Roger Reeves', 'rreeves@institution-name.edu', 'active'], ['1555554', '', 'wgriffin', '', 'Warren', 'Griffin', 'Warren Griffin', 'Griffin, Warren', 'Warren Griffin', 'wgriffin@institution-name.edu', 'active'], ['1555555', '', 'tsanders', '', 'Tammy', 'Sanders', 'Tammy Sanders', 'Sanders, Tammy', 'Tammy Sanders', 'tsanders@institution-name.edu', 'active'], ['1555556', '', 'cprice', '', 'Carrie', 'Price', 'Carrie Price', 'Price, Carrie', 'Carrie Price', 'cprice@institution-name.edu', 'active'], ['1555557', '', 'abowers', '', 'Alicia', 'Bowers', 'Alicia Bowers', 'Bowers, Alicia', 'Alicia Bowers', 'abowers@institution-name.edu', 'active'], ['1555558', '', 'eramsey', '', 'Essie', 'Ramsey', 'Essie Ramsey', 'Ramsey, Essie', 'Essie Ramsey', 'eramsey@institution-name.edu', 'active'], ['1555559', '', 'lwillis', '', 'Lila', 'Willis', 'Lila Willis', 'Willis, Lila', 'Lila Willis', 'lwillis@institution-name.edu', 'active'], ['1555560', '', 'csoto', '', 'Corey', 'Soto', 'Corey Soto', 'Soto, Corey', 'Corey Soto', 'csoto@institution-name.edu', 'active']]
'''

columns = ["user_id", "integration_id", "login_id", "password", "first_name",
            "last_name", "full_name", "sortable_name", "short_name",
            "email", "status"]
Student = namedtuple('Student', columns)
student_namedtupe_list = []

for row in student_list:
    student = Student(*row)
    student_namedtupe_list.append(student)

print(student_namedtupe_list[0])
print(student_namedtupe_list[0].full_name)
'''
Student(user_id='1555551', integration_id='', login_id='lrice', password='', first_name='Lonnie', last_name='Rice', full_name='Lonnie Rice', sortable_name='Rice, Lonnie', short_name='Lonnie Rice', email='lrice@institution-name.edu', status='active')
Lonnie Rice
'''
