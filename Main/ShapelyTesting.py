from shapely.geometry import Point, LineString, Polygon

point = Point(1.5, 2.0)

line = LineString([(0,0), (1.5, 2), (3, 4)])

polygon = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])

print("Point Area:", point.area)
print("Line Length:",  line.length)
print("Polygon Area:", polygon.area)