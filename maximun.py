#!/usr/bin/env python3

# Maximun algorithm
# By: lgarciaorozco6@gmail.com
# LICENSE GNU/GPL
# 9/10/23

from random import randint

n = 1e6
a = -1e5
b = 1e5

data = [randint(int(a),int(b)) for _ in range(int(n))]
m = None
if data:
    m = data[0]
    for x in data:
        if x >= m: m = x

print(m)
