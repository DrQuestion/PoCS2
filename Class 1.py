class Complex(object):
    def __init__(self, real, imaginary):
        self.r=real
        self.i=imaginary
    def __add__(self, other):
        return Complex(self.r+other.r,self.i+other.i)
    def __sub__(self, other):
        return Complex(self.r-other.r,self.i-other.i)
    def __mul__(self, other):
        return Complex(self.r*other.r-self.i*other.i,self.r*other.i+self.i*other.r)
    def __div__(self, other):
        return Complex((self.r*other.r+self.i*other.i)/(other.r**2+other.i**2),(self.i*other.r-self.r*other.i)/(other.r**2+other.i**2))
    def mod(self):
        return Complex((self.r**2+self.i**2)**0.5,0) #don't get why the modulus should still belong to Complex class
    def __str__(self):
        if self.i == 0:
            result = "%.2f+0.00i" % (self.r)
        elif self.r == 0:
            if self.i >= 0:
                result = "0.00+%.2fi" % (self.i)
            else:
                result = "0.00-%.2fi" % (abs(self.i))
        elif self.i > 0:
            result = "%.2f+%.2fi" % (self.r, self.i)
        else:
            result = "%.2f-%.2fi" % (self.r, abs(self.i))
        return result