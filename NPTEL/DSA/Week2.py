def primeproduct(n):
    i=2
    while i<n:
        if ifprime(i):
            if n%i == 0:
                if ifprime(n/i):
                    return True
        i=i+1
    return False 
  
def ifprime(k):
    p=2
    if (k==1):
        return 0
    while p<k:
        if k%p == 0:
            return 0
        else:
            if p<(k/p):
                p=p+1
            else: 
                break
    return 1  
  
  
def delchar(s,c):
    a= ""
    if len(c) != 1:
        return s
    else:
        for char in s:
            if char != c:
                 a = a + char
        return a
      
      
      
      
def shuffle(l1,l2):
    ln = [] 
    i = 0
    if (len(l1)>len(l2)):
        t = len(l1)
    else:
        t = len(l2)
    while(i < t ):
        if i < len(l1):
            ln.append(l1[i])
        if i < len(l2):
            ln.append(l2[i])
        i =i + 1   
    return ln  
import ast

def tolist(inp):
  inp = "["+inp+"]"
  inp = ast.literal_eval(inp)
  return (inp[0],inp[1])

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "primeproduct":
   arg = parse(farg)
   print(primeproduct(arg))
elif fname == "delchar":
   (s1,s2) = parse(farg)
   print(delchar(s1,s2))
elif fname == "shuffle":
   (l1,l2) = parse(farg)
   print(shuffle(l1,l2))
else:
   print("Function", fname, "unknown")
