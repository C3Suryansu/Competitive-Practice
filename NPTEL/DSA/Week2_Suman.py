def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primeproduct(n):
    flag=0
    if n<0 :
        return False
    p=[2]

    for i in range(3,n):
        if(is_prime(i)):
            p.append(i)
    for i in p:
        for j in p:
            if(i*j == n):
                flag=1
                return True
    if(flag==0):
        return False

def delchar(s,c):
    if(len(c)>1):
        return s
    return(s.replace(c,''))

def shuffle(a,b):
    c=[]
    n1=len(a)
    n2=len(b)
    if(n1>n2):
        n=n2
    else:
        n=n1
        
    for i in range(0,n):
        c.append(a[i])
        c.append(b[i])

    if(n1!=n2):
        if(n1>n2):
            c=c+a[n:]
        else:
            c=c+b[n:]
    return(c)
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
