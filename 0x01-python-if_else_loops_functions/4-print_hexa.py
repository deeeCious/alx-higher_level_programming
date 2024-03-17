#!/usr/bin/python3

print(*[f"{num} = 0x{num:x}" for num in range(99)], sep='\n')
