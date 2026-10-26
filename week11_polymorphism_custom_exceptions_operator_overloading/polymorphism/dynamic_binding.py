
class A:
    def hello():
        print('HELLO A')

class B(A):
    def hello():
        print('HELLO B')

class C(B):
    def hello():
        print('HELLO C')

def main():
    # A instance
    var1 = A()
    
    # B instance
    var2 = B()

    # C instance
    var3 = C()

    # Which version of hello() is called right now?
    var3.hello()

if __name__ == '__main__':
    main()