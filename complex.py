class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def __add__ (self,other):
        return Complex(self.real + other.real,self.imag + other.imag)
    def __sub__ (self,other):
        return Complex(self.real - other.real,self.imag - other.imag)
    def __mul__ (self,other):
        real = (self.real * other.real - self.imag * other.imag,)
print('hello ')