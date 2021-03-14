from collections import defaultdict
a_dict={}
a_dict.setdefault("missingkey","defaultvalue")
print(a_dict)
a_dict.get("a","b")
print(a_dict)
a_dict = {}
if 'key' in a_dict:
    # Do something with 'key'...
    a_dict['key']
else:
    a_dict['key'] = 'default value'

print(issubclass(defaultdict, dict))
a_dict=defaultdict(list)
a_dict["one"]=1
a_dict["missing"]
a_dict["anothermissing"].append(4)
def dic(a_dict):
 b=iter(a_dict.items())
 for i in next(b):
     print(next(b))

print(dic(a_dict))

"""a=a_dict.items()
b=iter(a)
c=next(b)

print(c)"""
dd=defaultdict(list)
dd["one"].append(1)
dd["two"].append(2)
dd["three"].append(3)
print(dd)
dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe')]

s=defaultdict(list)
for dep,employee in dep:
    s[dep].append(employee)
print(s)
"""depd = dict()
for department, employee in dep:
    depd.setdefault(department, []).append(employee)

print(depd)"""
dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe')]

uni=defaultdict(set)
for i, j in dep:
    uni[i].add(j)
print(uni)
rao=defaultdict(int)
for i, _ in dep:
    rao[i]+=1
 
print(rao)
from collections import Counter
counter=Counter(dep)
print(counter)
incomes = [('Books', 1250.00),
           ('Books', 1300.00),
           ('Books', 1420.00),
           ('Tutorials', 560.00),
           ('Tutorials', 630.00),
           ('Tutorials', 750.00),
           ('Courses', 2500.00),
           ('Courses', 2430.00),
           ('Courses', 2750.00),]
dd=defaultdict(float)
for product,income in incomes:
    dd[product]+=income
print(dd)
for product, income in dd.items():
    print(f'Total income for {product}: ${income:,.2f}')
print(dd)
dd=defaultdict(list, letters=["a", "b", "c"])
dd.default_factory
dd["numbers"].append(4)
print(dd)
dd['numbers'] += [2, 3]
print(dd)
