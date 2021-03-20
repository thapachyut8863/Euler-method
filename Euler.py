# function to be solved
def f(x,y):
    return ((y*y -x*x)/(y*y+x*x))
    #return y*(1+x*x)
    #return (y-x)/(y+x)
    #return x+y*y
    



# Euler method
def euler(a,y0,b,n):
    
    # Calculating step size
    h = (b-a)/n
    
    print('\n-----------OUTPUT-----------')
    print('------------------------------')    
    print('x0\ty0\tslope\tyn')
    print('------------------------------')
    for i in range(n):
        slope = f(a, y0)
        yn = y0 + h * slope
        print('%.4f\t%.4f\t%0.4f\t%.4f'% (a,y0,slope,yn) )
        print('------------------------------')
        y0 = yn
        a = a+h
    
    print('\nAt x=%.4f, y=%.4f' %(b,yn))

# Inputs
print('Enter initial conditions:')
a = float(input('a = '))
y0 = float(input('y0 = '))

print('Enter calculation point: ')
b = float(input('b = '))

print('Enter number of steps:')
step = int(input('Number of steps = '))

# Euler method call
euler(a,y0,b,step)