# -*- coding: utf-8 -*-
"""Untitled38.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lVGYzjRqf81TI6FKlE6YL9DHcPAvR4NL
"""

t = int(input())
for _ in range(t):
    n = int(input())
    c = 1
    nums = list(map(int, input().split()))
    for i in range(n):
      print(c * abs(nums[i]),end = " ")
      c *= -1
    print()
