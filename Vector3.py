class Vector():
    def __init__(self, s='0,0'):
        A = s.split(',')
        self.x = float(A[0])
        self.y = float(A[1])
    def __str__(self):
        return '(' + str(self.x) + ','+ str(self.y) + ')'
    def __add__(self, other):
        return Vector(str(self.x + other.x) + ',' + str(self.y + other.y))
    def __sub__(self, other):
        return Vector(str(self.x - other.x) + ',' + str(self.y - other.y))
    def __mul__(self, other):
        return Vector(str(self.x * other) + ',' + str(self.y * other))
    def __truediv__(self, other):
        return Vector(str(self.x / other) + ',' + str(self.y / other))
    def dist(self):
        return (self.x**2 + self.y**2)**(0.5)
n = int(input())
a = []
for i in range(n):
    a.append(Vector(input()))
def CM(a):
    S=Vector('0,0')
    for i in a:
        S=S+i
    return S/len(a)
print('CENTER_MASS',CM(a))