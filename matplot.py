from matplotlib.pyplot import *
from numpy import *

x = [1,2,3,4,5,6]
p1 = (-1, 5)

plot(x, polyval(p1,x))
show()