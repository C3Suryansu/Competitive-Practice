for _ in range(int(input())):
  a0, a1, a2 = map(int, input().split())
  b0, b1, b2 = map(int, input().split())
  res = 0
  m = min(a0, b2)
  a0 -= m
  b2 -= m

  m = min(a1, b0)
  a1 -= m
  b0 -= m

  res += 2*min(a2,b1)
  res -= 2 * min(a1, b2)
  print(res)
