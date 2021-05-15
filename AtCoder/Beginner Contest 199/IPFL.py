#https://atcoder.jp/contests/abc199/tasks/abc199_c

n = int(input())
s = list(input())
q = int(input())
c = 0
 
for i in range(q):
  t, a, b = map(int, input().split())
  if t == 1:
    if c%2:
      if a >= n:
        a -= n
      else:
        a += n
      
      if b >= n:
        b -= n
      else:
        b += n
        
    s[a-1], s[b-1] = s[b-1], s[a-1]
  else:
    c += 1
if c % 2 == 0:
	print("".join(s))
else:
  s = s[n:] + s[:n]
  print("".join(s))
