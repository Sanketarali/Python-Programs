class A:  
    def displayA(self):
        print("HellO A")
class B(A):
    def displayB(self):
        print("Hello B")
obj=B()
obj.displayA()
obj.displayB()
