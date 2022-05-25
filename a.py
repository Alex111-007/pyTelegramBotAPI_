import math
from math import sqrt

a = float(input("катет1: "))
b = float(input("гипотенуза: "))

gip2= (b ** 2) - (a ** 2)
gip1 = sqrt(gip2)
print(gip1)