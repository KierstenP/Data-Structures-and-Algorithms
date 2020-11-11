class Vector:
    def __init__(self, d):
        if isinstance(d, list):
            self.coords = d
        else:
            self.coords = [0] * d

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if(len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return "<"+ str(self.coords)[1: -1] + ">"

    def __repr__(self):
        return str(self)

    def __sub__(self, other):
        if(len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        negativeResult = Vector(len(self))
        for i in range(len(self)):
            negativeResult[i] = (-1 * (self[i]))
        return negativeResult

    def __mul__(self, n):
        if isinstance(n, Vector):
            if (len(self) != len(n)):
                raise ValueError("dimensions must agree")
            dotProduct = 0
            for i in range(len(self)):
                dotProduct += (self[i] * n[i])
            return dotProduct
        else:
            scalarProduct = Vector(len(self))
            for i in range(len(self)):
                scalarProduct[i] = (n * self[i])
            return scalarProduct

    def __rmul__(self, num):
        multipliedResult = Vector(len(self))
        for i in range(len(self)):
            multipliedResult[i] = (num * self[i])
        return multipliedResult

def main():
    v1 = Vector(5)
    v1[1] = 10
    v1[-1] = 10
    print(v1)
    print()
    v2 = Vector([2, 4, 6, 8, 10])
    print(v2)
    print()
    u1 = v1 + v2
    print(u1)
    print()
    u2 = -v2
    print(u2)
    print()
    u3 = 3 * v2
    print(u3)
    print()
    u4 = v2 * 3
    print(u4)
    print()
    u5 = v1 * v2
    print(u5)
    print()



        


