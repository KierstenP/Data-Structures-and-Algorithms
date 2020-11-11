import random

class UnsortedArrayMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    def __init__(self):
        self.table = []

    def __len__(self):
        return len(self.table)

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        for item in self.table:
            if key == item.key:
                return item.value
        raise KeyError("Key Error: " + str(key))

    def __setitem__(self, key, value):
        for item in self.table:
            if key == item.key:
                item.value = value
                return
        self.table.append(UnsortedArrayMap.Item(key, value))

    def __delitem__(self, key):
        for j in range(len(self.table)):
            if key == self.table[j].key:
                self.table.pop(j)
                return
        raise KeyError("Key Error: " + str(key))

    def __iter__(self):
        for item in self.table:
            yield item.key


class ChainingHashTableMap:

    def __init__(self, N=55, p=123456789):
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        self.c = p
        self.a = random.randrange(1, self.p - 1)
        self.b = random.randrange(0, self.p - 1)

    def hash_function(self, k):
        return ((self.a * hash(k) + self.b) % self.p) % self.N

    def __len__(self):
        return self.n

    def __getitem__(self, key):
        i = self.hash_function(key)
        current_bucket = self.table[i]
        if current_bucket is None:
            raise KeyError("Key Error: " + str(key))
        try:
            return current_bucket[key]
        except Exception:
            return current_bucket.value

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        if self.table[i] is None:
            self.table[i] = UnsortedArrayMap().Item(key,value)
        elif type(self.table[i]) != "class '__main__.UnsortedArrayMap'>":
            prev_item = self.table[i]
            self.table[i] = UnsortedArrayMap()
            self.table[i][prev_item.key] = prev_item.value
        if self.table[i] == "class '__main__.UnsortedArrayMap'>":
            old_size = len(self.table[i])
            self.table[i][key] = value
            new_size = len(self.table[i])
            if (new_size > old_size):
                self.n += 1
            if (self.n > self.N):
                self.rehash(2 * self.N)

    def __delitem__(self, key):
        i = self.hash_function(key)
        current_bucket = self.table[i]
        if current_bucket is None:
            raise KeyError("Key Error: " + str(key))
        if type(current_bucket)== "class '__main__.UnsortedArrayMap'>":
            del current_bucket[key]
            if len(current_bucket)== 1:
                for leftover_key in current_bucket:
                    leftover = leftover_key
                curr_bucket = UnsortedArrayMap().Item(leftover,current_bucket[leftover])
            self.n -= 1
            if (current_bucket.is_empty()):
                self.table[i] = None
            if (self.n < self.N // 4):
                self.rehash(self.N // 2)
        else:
            current_bucket.key = None
            current_bucket.value = None
    def __iter__(self):
        for current_bucket in self.table:
            if (current_bucket is not None):
                for key in current_bucket:
                    yield key

    def rehash(self, new_size):
        old = []
        for key in self:
            value = self[key]
            old.append((key, value))
        self.table = [None] * new_size
        self.n = 0
        self.N = new_size
        for (key, value) in old:
            self[key] = value


