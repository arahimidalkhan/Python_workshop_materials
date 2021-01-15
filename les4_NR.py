import math
x0=-3;
xn=x0
fn=xn**3 - 2*xn**2+10-200*math.sin(xn)
fxn=3*xn**2 - 4*xn-200*math.cos(xn)
xn1=xn-fn/fxn
err=1e-20
itr=1
while abs(xn1-xn)>err:
    xn=xn1
    fn=xn**3 - 2*xn**2+10-200*math.sin(xn)
    fxn=3*xn**2 - 4*xn-200*math.cos(xn)
    xn1=xn-fn/fxn
    itr +=1
print(itr,xn)

## The second solution
import math
def f(x):
    return (x**3 - 2*x**2+10-200*math.sin(x))
def df(x):
    return (3*x**2 - 4*x-200*math.cos(x))
x0=-3;
xn=x0
xn1=xn-f(xn)/df(xn)
err=1e-20
itr=1
while abs(xn1-xn)>err:
    xn=xn1
    xn1=xn-f(xn)/df(xn)
    itr +=1
print(itr,xn)

## The third solution
def f(x):
    return (x**3 - 2*x**2+10-200*math.sin(x))
from scipy import optimize
root = scipy.optimize.newton(f, -3)
print(root)