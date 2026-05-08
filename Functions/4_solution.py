import math
def stats(radius):
   area=math.pi * radius **2;
   circumference=2*math.pi*radius;
   return area,circumference;

a,c=stats(2)
print('area',a,'circumference',c)