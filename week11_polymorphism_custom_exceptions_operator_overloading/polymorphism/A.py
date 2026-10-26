class A:
    def __init__(self, a, b):
        self.__a = a 
        self.__b = b

    def __len__(self):
        return self.__a + self.__b

a1 = A(10, 20)

print(len(a1))
print(a1)
print(a1.len())