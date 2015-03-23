'''simple exponentation, accurate to about 6 decimal places
'''
def pow(mantissa, exponent, precision=0.00000000001):
    if exponent < 0:
        return 1/pow(mantissa, -exponent, precision)
    elif (exponent >= 10): 
        result = pow(mantissa, exponent/2, precision/2)
        return result*result
    elif (exponent >= 1):
        return mantissa * pow(mantissa, exponent-1, precision)
    elif precision >=1:
        return sqrt(mantissa)
    else:
        return sqrt(pow(mantissa, exponent*2, precision*2))

def sqrt(mantissa, precision=35000):
    approximation = precision*10
    for i in range(0, precision):
        approximation = 0.5*(approximation + (mantissa/approximation))
    return approximation

###

'''exponentation by squaring
'''
def integer_pow(x,n):
    total = 1
    for i in range(0,n):
        total*=x
    return total

'''simple iterative version of factorial
'''
def fact(num):
    f = 1
    for i in range(2, num+1):
        f *= i
    return f

'''approximation using taylor series
'''
def ln(x, precision=170):
    if precision >=1:
        return integer_pow((x-1)/x, precision)/precision+ln(x, precision-1)
    return 0


'''approximation using taylor series
'''
def exp(x, precision=170):
    if precision >=1:
        return integer_pow(x, precision)/fact(precision)+exp(x, precision-1)
    else:
        return 1


'''uses identity x^n = e^(n ln x). Accuracy largely depends on implementation of exp and ln - in my case they are implemented through Taylor series.
accurate to ~ 2 decimal places
    
'''
def pow_by_identity(mantissa, exponent):
    return exp(exponent*ln(mantissa))