class calculate:
    def rectangle(self,a,b):
        self.a=a
        self.b=b
        pr=2*a*b
        ar=a*b
        print("perimeter of rectangle=",pr)
        print("area of rectangle=",ar)
    def circle(self,c):
        self.c=c
        pr=2*3.14*c
        ar=3.14*c*c
        print("perimeter of circle=",pr)
        print("area of circle=",ar)
    def triangle(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        pr=a*b*c
        ar=0.5*a*b*c
        print("perimeter of triangle=",pr)
        print("area of triangle=",ar)
obj=calculate()
obj.rectangle(2,4)
obj.circle(3)
obj.triangle(2,5,6)

