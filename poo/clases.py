class Book:
    titulo:str
    autor:str
    year:int
    
    def __init__(self, titulo, autor, year):
        self.titulo = titulo
        self.autor = autor
        self.year = year

class Rect:
    base:float
    height:float
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calc_area(self):
        print(self.base * self.height)
        
class Calc:
    n1:float
    n2:float
    
    
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def add(self):
        print(self.n1 + self.n2)
        
    def rest(self):
        print(self.n1 - self.n2)
        
    def divide(self):
        print(self.n1 / self.n2)
        
    def multiply(self):
        print(self.n1 * self.n2)
