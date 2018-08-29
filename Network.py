'''a = input()
s = set()
def update_dictionary(d, key, value):
    a = key * 2
    if key in d:
        d.setdefault(key, []).append(value)
    else:
        if a in d:
            d.setdefault(a, []).append(value)
        else:
            d.update({a: [value]})
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)
''''''

a = input().lower().split()
t = {}
for i in range (len(a)):
    d = a.count(a[i])
    t.update({a[i]:d})
for key, value in t.items():
    print(key, value, end=" ")
    print()
'''
'''def f(x):
   x = x**3
   return (x)
n = int(input())
t = {}
for i in range (n):
    x = int(input())
    if  x not in t:
        c = f(x)
        t.update({x:c})
        'for x in t.keys():'
        print(t[x])
    else:
        'for x in t:'
        print(t[x])

prin
'''
'''with open('dataset_3363_2.txt', 'r') as inf:
    s1 = inf.readline().strip()
    l = len(s1)
    i = 0
    while i != l:
       print (s1[i+1])
       if s1[i+1].isdigit == 'true':
           print(2)
           if s1[i+2].isdigit == 'true':
                t = int(s1[i+1])*10 + int(s1[i+2])
                d = s1[i] * t
                print(d)
                with open('dataset_3363_1.txt', 'w') as ouf:
                    ouf.write(d)
                i+=3
           elif s1[i+2].isdigit == 'false':
                t = int(s1[i + 1])
                d = s1[i] * t
                print(d)
                with open('dataset_3363_1.txt', 'w') as ouf:
                    ouf.write(d)
                i+=2'''


'''with open('dataset_3363_2.txt', 'r') as inf:
    s1 = inf.readline().strip()
    l = len(s1)
    i = 0
    d = []
    while i < l:
        print(s1[i+1])
        print(i)
        print(s1[i+1].isdigit())
        print(s1[i+2].isdigit())
        a = '1'
        b = 'a'
        p = a.isdigit()
        m = b.isdigit()
        if (s1[i+1].isdigit()) == p and (s1[i+2].isdigit() == m):
            print(2)
            t = int(s1[i + 1])
            d.append(s1[i] * t)
            with open('dataset_3363_1.txt', 'a') as ouf:
                ouf.write(s1[i] * t)
            print(d)
            i += 2
        elif s1[i+2].isdigit() == p and s1[i+2].isdigit() == p:
            t = int(s1[i+1])*10 + int(s1[i+2])
            d.append(s1[i] * t)
            with open('dataset_3363_1.txt', 'a') as ouf:
                ouf.write(s1[i] * t)
            print(d)
            i+=3'''
'''
with open('dataset_3363_2.txt', 'a') as ouf:
    ouf.write('\n')
with open('dataset_3363_2.txt', 'r') as inf:
    s1 = inf.readline()
    l = len(s1)
    i = 0
    d = []
    while i < l:
        print (i)
        a = '1'
        b = 'a'
        p = a.isdigit()
        m = b.isdigit()
        if s1[i+1].isdigit() == p and s1[i+2] == '\n':
            t = int(s1[i + 1])
            with open('dataset_3363_1.txt', 'a') as ouf:
                ouf.write(s1[i] * t)
            break
        elif s1[i+1].isdigit() == p and s1[i+2].isdigit() == m:
            t = int(s1[i + 1])
            with open('dataset_3363_1.txt', 'a') as ouf:
                ouf.write(s1[i] * t)
            i += 2
        elif s1[i+1].isdigit() == p and s1[i+2].isdigit() == p:
            t = int(s1[i+1])*10 + int(s1[i+2])
            with open('dataset_3363_1.txt', 'a') as ouf:
                ouf.write(s1[i] * t)
            i+=3'''
'''
import math
pi = math.pi
r = input()
print(2*pi*r)'''
'''import sys
list = [sys.argv]
print (*list)

import sys
l = [sys.argv]
d = len(l)
for i in range (d):
    print(l[i])
    print(i)
    i+=1'''

import shutil
shutil.rmtree('\\\\192.168.40.195\\Network Recycle Bin 1\\', True)
shutil.rmtree('\\\\192.168.40.195\\Network Recycle Bin 3\\TEALL\\')
shutil.rmtree('\\\\192.168.40.195\\Network Recycle Bin 7\\', True)
shutil.rmtree('\\\\192.168.40.195\\Network Recycle Bin 9\\', True)