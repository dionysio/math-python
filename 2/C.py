from math import sqrt


'''ok for low numbers, sucks for anything higher
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

'''exponentation by squaring
'''
def integer_pow(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    elif n % 2: #odd case
        return x * integer_pow(x*x, (n-1)/2)
    else:
        return integer_pow(x*x, n/2)

'''approximation using taylor series
'''
def ln(x, precision=100):
    if precision >=1:
        return integer_pow((x-1)/x, precision)/precision+ln(x, precision-1)
    return 0

'''simple iterative version of factorial
'''
def fact(num):
    f = 1
    for i in range(2, num+1):
        f *= i
    return f

'''approximation using taylor series
'''
def exp(x, precision=100):
    if precision >=1:
        return integer_pow(x, precision)/fact(precision)+exp(x, precision-1)
    else:
        return 1


def sqrt(mantissa):
    return pow_by_identity(mantissa, 0.5)


'''uses identity x^n = e^(n ln x)
    much more precise than first pow
'''
def pow_by_identity(mantissa, exponent):
    return exp(exponent*ln(mantissa))