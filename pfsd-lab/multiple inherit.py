
class rectangle(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
class circle(object):
    def __init__(self,c):
        self.c=c
class triangle(object):
    def __init__(self,d,e,f):
        self.d=d
        self.e=e
        self.f=f
class shapes(rectangle,circle,triangle):
    def __init__(self,a,b,c,d,e,f):
        rectangle.__init__(self,a,b)
        circle.__init__(self,c)
        triangle.__init__(self, d, e, f)
        print("perimeter of rectangle=",2*a*b)
        print("area of rectangle=",a*b)
        print("perimeter of circle=",3.14*c*c)
        print("area of circle=",2*3.14*c)
        print("perimeter of triangle=",d*e*f)
        print("area of triangle=",0.5*d*e*f)
obj=shapes(1,2,3,4,5,6)









