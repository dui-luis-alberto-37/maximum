#!/usr/bin/env python3

# Maximun algorithm
# By: lgarciaorozco6@gmail.com
# LICENSE GNU/GPL
# 9/10/23

from random import random

n = 1e6

data = [random() for _ in range(int(n))]

m = None
if data:
    m = data[0]
    for x in data:
        if x >= m: m = x

print(m)
