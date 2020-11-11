import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.n = 0
        self.capacity = 1

    def append(self, val):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data[i]
        self.data = new_arr
        self.capacity = new_size

    def __len__(self):
        return self.n

    def __getitem__(self, ind):
        if not(0 <= ind <= (self.n - 1)):
            ind = self.n + ind
        elif not(ind < 0 or ind > self.n-1):
            raise Exception
        return self.data[ind]

    def __setitem__(self, ind, val):
        if not(0 <= ind <= (self.n - 1)):
            ind = self.n + ind
        self.data[ind] = val

    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]

    def extend(self, iterable_collection):
        for elem in iterable_collection:
            self.append(elem)

    def __add__(self, other):
        newlst = MyList()
        newlst += self
        newlst += other
        return newlst

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __mul__(self, other):
        lst = MyList()
        for i in range(other):
            lst.extend(self)
        return lst

    def __rmul__(self, other):
        return self * other

    def __repr__(self):
        return "[" + ", ".join([str(elem) for elem in self]) + "]"

    def insert(self, index, val):
        afterIndexLst = self.data[index:]
        count = 1
        try:
            if index < 0:
                index = len(self) + index
            if index > self.capacity + 1 :
                raise IndexError
            else:
                if self.n == self.capacity:
                    self.resize((2 * self.capacity))
                self.data[index] = val
            self.append(0)
            for val in afterIndexLst:
                self.data[index+count] = val
                count += 1

        except IndexError:
            print("The index is out of range.")
        print(self)


    def pop(self):
        try:
            if self.n == 0:
                raise IndexError
            else:
                count = 0
                lastIndex = len(self)-1
                while(lastIndex>=0):
                    if lastIndex == None:
                        self.n -= 1
                        count += 1
                        lastIndex -= 1
                    else:
                        returnValue = self[lastIndex]
                        self.data[lastIndex] = None
                        count += 1
                        break
                if (self.n - count) < (self.capacity//4):
                    self.resize(self.capacity//2)
                return returnValue
        except IndexError:
            print("List is empty.")




