class Iterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else: raise StopIteration

n = int(input("Enter value of N:"))

numbers = Iterator(n)

for num in numbers:
    print(num)