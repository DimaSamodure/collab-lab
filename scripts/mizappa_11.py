import math
def solve(a,b,c):
    d=b*b-4*a*c
    if d<0:
        return "No real roots"
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    return r1,r2
print(solve(1,-3,2))
print(solve(1,2,1))
print(solve(1,0,1))
