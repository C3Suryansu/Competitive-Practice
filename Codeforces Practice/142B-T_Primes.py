lim = 10**6
val = [1] * lim
a = set()
a.add(4)
for i in range(2, lim):
  if val[i]:
    for j in range(i*i, lim, i):
      val[j] = 0
    a.add(i*i)
input()
for i in list(map(int, input().split())):
  if i in a:
    print("YES")
  else:
    print("NO")
    
#Approach :- Triple positive factors can only be possible for square of a prime number, and range is root of max val, root 10^12 = 10^6, thus, using Sieve of Eratosthenes
#And adding i*i to the set, we create a set, and thus check the inputs existence in the set.
