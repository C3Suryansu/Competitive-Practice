for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  min_a = min(a)
  min_b = min(b)
  res = 0

  for i in range(n):
    res += max(a[i] - min_a, b[i] - min_b)
  print(res)
