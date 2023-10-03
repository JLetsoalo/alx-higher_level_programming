#!/usr/bin/python3
for x in range(ord('z'), ord('a')-1, -1):
    print('{:c}'.format(x) if x % 2 == 0 else chr(x-32), end='')
