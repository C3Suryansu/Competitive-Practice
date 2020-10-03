def isPrime(n):
    if (n <= 1) :  
        return False
    if (n <= 3) :  
        return True
    if (n % 2 == 0 or n % 3 == 0) :  
        return False 
    i = 5
    while(i * i <= n) :  
        if (n % i == 0 or n % (i + 2) == 0) :  
            return False
        i = i + 6
    return True


def primeproduct(m):
    if m > 0:
        i=2
        k=0
        while i**2<=m:
            if m%i==0:
                if not (isPrime(i) and isPrime(m/i)):
                    k=-1
                    break
            i=i+1
        if k==-1:
            return False
        elif k==0:
            return True
    else:
        return False
#------------------------------------
def delchar(s, c):
    if len(c)==1:
        return s.replace(c,'')
    else:
        return s

#-------------------------------------

def shuffle(l1, l2):
  l3 = []
  if len(l1) == len(l2):
    for i in range(len(l1)):
      l3.append(l1[i])
      l3.append(l2[i])
  elif len(l1) < len(l2):
    for i in range(len(l1)):
      l3.append(l1[i])
      l3.append(l2[i])
    for i in l2[len(l1):]:
      l3.append(i)
  else:
    for i in range(len(l2)):
      l3.append(l1[i])
      l3.append(l2[i])
    for i in l1[len(l2):]:
      l3.append(i)
  return l3
