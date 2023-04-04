class A:  
    def displayA(self):
        print("HellO A")
class B(A):
    def displayB(self):
        print("Hello B")
class C(B):
    def displayC(self):
        print("Hello C")


obj=C()
obj.displayA()
obj.displayB()
obj.displayC()
