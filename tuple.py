point = (1, "Hello", 10)
print(point[0])
print(point[1])
print(point[2])

def distance(pointA, pointB):
    return (((pointA[0] - pointB[0]) ** 2) + ((pointA[1] - pointB[1]) ** 2)) ** 0.5

pointA = 1, 7
pointB = 1, 10
d = distance(pointA,pointB)
print(d)