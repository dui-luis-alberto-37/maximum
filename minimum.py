#!/usr/bin/env python3

# Minimun algorithm
# By: lgarciaorozco6@gmail.com
# LICENSE GNU/GPL
# 9/10/23


from random import random

n = 1e6

data = [random() for _ in range(int(n))]

if data:
    m = data[0]
    for x in data:
        if x <= m: m = x
else: m = None

print(m)
