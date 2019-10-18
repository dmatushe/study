class Turtle:
    def __init__(self, x, y):
        self.pos = (x, y)
    
    def where(self):
        print(f'Я в {self.pos}')

    def setx(self, x):
        self.pos = (x, self.pos[1])

    def sety(self, y):
        self.pos = (self.pos[0], y)

    def __str__(self):
        return f"Я черепашка в {self.pos}"

t = Turtle(0, 2)
print(t)
t.where()
t.setx(15)
t.where()

class LazyTurtle(Turtle):
    
    def setx(self, x):
        if abs(self.pos[0] - x) > 10:
            print("Мені ліньки...")
        else:
            super(LazyTurtle, self).setx(x)
    
    def sety(self, y):
        if abs(self.pos[1] - y) > 10:
            print("Мені ліньки...")
        else:
            super(LazyTurtle, self).setx(y)

p = LazyTurtle(1, 5)
p.setx(40)
p.where()