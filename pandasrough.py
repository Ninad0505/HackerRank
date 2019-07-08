import pandas as pd
from matplotlib.pyplot import *
from numpy import *


weather_data = {

    'temp' : [12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
    'windspeed' : [1,6,3,4,5,6,7,8,9,20,11,12,13,6,15,16]

}
df = pd.DataFrame(weather_data)

df['one'] = df['temp'] - df['temp'].mean()
df['two'] = df['windspeed'] - df['windspeed'].mean()

df['12'] = df['one']*df['two']
df['1sq'] = df['one']**2

m = df['12'].sum()/df['1sq'].sum()
print(m)
c = -m*df['temp'].mean() + df['windspeed'].mean()
print(c)

p1 = (m, c)
plot( df['temp'], polyval(p1, df['temp']))
plot( df['temp'], df['windspeed'], 'o')
show()

