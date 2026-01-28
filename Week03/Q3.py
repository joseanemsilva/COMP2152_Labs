# Question 3: Coordinate System (Tuples - Creation and Unpacking)

point1 = (3,5)
point2 = (7,2)
print(f"Point is: {point1}\nPoint2 is: {point2}\n")

x1, y1 = point1
x2, y2 = point2
print(f"x1= {x1}, y1= {y1}\nx2= {x2}, y2= {y2}\n")

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"Distance between points: {distance}\n")