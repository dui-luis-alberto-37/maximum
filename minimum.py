#!/usr/bin/env python3

# Maximun algorithm
# By: lgarciaorozco6@gmail.com
# LICENSE GNU/GPL
# 9/10/23


data = [15.4,551.5,5.5,68.4,6.0]
m = None
if data:
    m = data[0]
    for x in data:
        if x <= m: m = x

print(m)
