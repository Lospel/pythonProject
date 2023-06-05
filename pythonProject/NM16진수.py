# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
a = user_input.split(" ")
N = int(a[0],16)
M = int(a[1],16)
answer = hex(N+M)
print(answer[2:])