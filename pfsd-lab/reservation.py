class counter(object):
    def __init__(self,source,destin):
        self.source=source
        self.destin=destin
class details(object):
    def __init__(self,name,age,gender,phno):
        self.name=name
        self.age=age
        self.gender=gender
        self.phno=phno
class traindetails(object):
    def __init__(self,noofpersons,trainno):
        self.noofpersons=noofpersons
        self.trainno=trainno
class display(object):
    def __init__(self,source,destin,name,age,gender,phno,noofpersons,trainno):
        counter.__init__(self,source, destin)
        details.__init__(self, name, age, gender, phno)
        traindetails.__init__(self, noofpersons, trainno)
        print("cost of your ticket=",int(noofpersons)*500)
        print("tickets are booked you ca check your mail and pay money through online")
obj=display(input("enter source:"),input("enter destination:"),input("enter name:"),
input("enter age:"),input("enter gender:"),input("enter phno:"),input("enter no of passengers"),
input("enter train no:"))




