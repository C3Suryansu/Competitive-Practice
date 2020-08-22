for _ in range(int(input())):
  n, k = map(int, input().split())
  if n < k:
    print(k - n)
  elif (n - k) % 2 == 0:
    print(0)
  else:
    print(1)
# if n less than k, we move k to nth point
# if not, say B is at m, so, (n-m)-(m-0) = k => n-2m = k => n-k = 2m => m = (n-k)/2
# Now, as m has to be an integer, if (n-k)/2 holds true, print 0 since it satisfies
# Else, print 1 cause we have to move n by 1 position to make it an integer.
