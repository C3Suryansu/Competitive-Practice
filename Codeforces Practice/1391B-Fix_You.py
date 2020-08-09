for _ in range(int(input())):
  c = 0
  n, m = map(int, input().split())
  for i in range(n - 1):
    s = input()
    if s[-1] == "R":
      c += 1

  s = input()
  c += s.count("D")
  print(c)
