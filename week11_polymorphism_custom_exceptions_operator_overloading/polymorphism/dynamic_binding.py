class A:
    # def hello(self):
    #     print('HELLO A')
    pass
class B(A):
    # def hello(self):
    #     print('HELLO B')
    pass

class C(B):
    # def hello(self):
    #     print('HELLO C')
    pass

def main():
    # A instance
    var1 = A()
    
    # B instance
    var2 = B()

    # C instance
    var3 = C()

    # Which version of hello() is called right now?
    #var3.hello()

    print(isinstance(var3, A))

if __name__ == '__main__':
    main()