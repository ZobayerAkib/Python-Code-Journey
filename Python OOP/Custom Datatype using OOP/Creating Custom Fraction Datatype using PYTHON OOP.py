class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.dnum=d
    #<==========================================================>
    def __str__(self):
        return "{}/{}".format(self.num,self.dnum)

    # <==========================================================>
    def __add__(self, other):
        temp_num=self.num*other.dnum + other.num*self.dnum
        temp_dnum=self.dnum*other.dnum
        return "{}/{}".format(temp_num,temp_dnum)

    # <==========================================================>
    def __sub__(self, other):
        temp_num=self.num*other.dnum - other.num*self.dnum
        temp_dnum=self.dnum*other.dnum
        return "{}/{}".format(temp_num,temp_dnum)

    # <==========================================================>
    def __mul__(self, other):
        temp_num=other.num*self.num
        temp_dnum=self.dnum*other.dnum
        return "{}/{}".format(temp_num,temp_dnum)

    # <==========================================================>
    def __truediv__(self, other):
        temp_num=other.dnum*self.num
        temp_dnum=self.dnum*other.num
        return "{}/{}".format(temp_num,temp_dnum)
    # <==========================================================>


x=Fraction(2,5)
y=Fraction(5,6)
print(x,y)
print(x+y)
print(x*y)
print(x-y)
print(x/y)