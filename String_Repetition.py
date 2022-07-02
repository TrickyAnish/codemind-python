import math
import os
import random
import re
import sys
s=input()
n=int(input())
def repeatedString(s, n):
    r = 0
    l = len(s)
    for i in range(0, l):
        if s[i] == 'a':
            r+= 1
    r*= int(n / l)
    for i in range(0, n % l):
        if s[i] == 'a':
            r+= 1
    return r
    
print(repeatedString(s, n))