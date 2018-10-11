def gcd(x,y):
    if(x!=0):
        r=y%x
        y=x
        x=r
        i=gcd(x,y)
        return i
    else:
        i=y
        return i

def recursive_gcd(x,y):
    if y == 0:
        return x
    else:
        return recursive_gcd(y, x % y)

print("enter two values: ")
x = input("x= ")
y = input("y= ")
if(x < y):
    print("the gcd of ",x," and ",y," is ",gcd(x,y))
    print("gcd found in recursive way ", recursive_gcd(x,y))
else:
    print("the gcd of ",x," and ",y," is ",gcd(y,x))
    print("gcd found in recursive way ", recursive_gcd(x,y))

