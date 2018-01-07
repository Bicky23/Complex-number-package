from math import atan

class complex_number(object):
    
    def __init__(self,x,y):
        
        if (type(x) == float or type(x) == int) and (type(y) == float or type(y) == int):
            self.real = x
            self.imag = y
        else:
            print('The number is invalid')
            
    def __repr__(self):
        
        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))
    
    def __add__(self, other):
        return complex_number(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return complex_number(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        return complex_number(self.real*other.real - self.imag*other.imag, self.real*other.imag + self.imag*other.real)
    
    def __truediv__(self, other):
        if other.real*other.real + other.imag*other.imag != 0:
            return ((self.real*other.real + self.imag*other.imag) / (other.real*other.real + other.imag*other.imag), 
                             (self.imag*other.real - self.real*other.imag) / (other.real*other.real + other.imag*other.imag))
        else:
            return "Denominator is zero."
    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5
    
    def real_part(self):
        return self.real
    
    def imaginary_part(self):
        return self.imag
    
    def argument(self):
        return math.atan(self.imag/self.real)
        
    def conjugate(self):
        return complex_number(self.real, -self.imag)
        
        
        
    