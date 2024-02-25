'''class A:
    def hi(self):
        print('hi')
    def hi(self,data):
        print("hello")
a=A()
a.hi(4)'''

class A:
    def hi(self):
        print('hi')
    def hi(self,data):
        print("hello")
class B:
    def hi(self,data):
        print('hi')
a=A()
b=B()
a.hi(4)
b.hi(5)
