#!/usr/bin/env python3
import time
import random
import sys
import subprocess
m = 256

n = int(sys.argv[1])

print(n)

first = ''.join(str(random.randrange(0,2)) for _ in range(m-1))+'1'
last = ''

for i in first:
    if i == '1':
        last+='0'
    else:
        last+='1'

print(first)

for _ in range(n-2):
    print(''.join(str(random.randrange(0,2)) for _ in range(m-1))+'1')

print(last)


