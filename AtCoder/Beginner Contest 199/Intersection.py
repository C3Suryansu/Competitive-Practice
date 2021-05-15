#https://atcoder.jp/contests/abc199/tasks/abc199_b

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
max_a = max(a)
min_b = min(b)
 
if max_a == min_b:
  print(1)
elif max_a > min_b:
  print(0)
else:
  print(abs(min_b - max_a) + 1)
