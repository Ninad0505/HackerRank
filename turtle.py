import turtle as t
name = 0
points = 1
pop = 2
state = [ 'COLORADO', [[-109,37],[-109,41],[-102,37],[-102,41]], 5187582]
cities = []
cities.append(['DENVER', [-104.98, 39.74], 634265])
cities.append(['DURANGO', [-107.88, 37.28], 17069])
cities.append(['BOULDER', [-105.27, 40.02], 98889])

map_width = 400
map_height = 300

minx = -180
maxx = 180
miny = -90
maxy = 90

for x,y in state[points] :
    if x < minx: minx = x
    elif x > maxx: maxx = x
    if y < miny: miny = y
    elif y > maxy: maxy = y

dist_x = maxx - minx
dist_y = maxy - miny
x_ratio = map_width/dist_x
y_ratio = map_height/dist_y

def convert(point):
    lon = point[0]
    lat = point[1]
    x = map_width - ((maxx - lon)*x_ratio)
    y = map_height - ((maxy - lat)*y_ratio)
    x = x - (map_width/2)
    y = y - (map_height/2)
    return [x,y]

t.up()
first_pixel = None
for point in state[points]:
    pixel = convert(point)
    if not first_pixel:
        first_pixel = pixel
    t.goto(first_pixel)
    t.down()
t.goto(first_pixel)
t.up()
t.goto([0,0])
t.write(state[name], align = 'center', font = ('Ariel', 16, 'bold'))