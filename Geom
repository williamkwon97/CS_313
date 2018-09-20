
#  File: Geom.py

#  Description: Using python to calculate Geometry

#  Student Name:William Kwon

#  Student UT EID:uk669

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:51350

#  Date Created:9/15

#  Date Last Modified:9/17
import math

class Point(object):
    # constructor
    # x and y are floats
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get distance
    # other is a Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # get a string representation of a Point object
    # takes no arguments
    # returns a string
    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    # test for equality
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-16
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


class Circle(object):
    # constructor
    # x, y, and radius are floats
    def __init__(self, radius=1, x=0, y=0):
        self.radius = radius
        self.center = Point(x, y)

    # compute cirumference
    def circumference(self):
        return 2.0 * math.pi * self.radius

    # compute area
    def area(self):
        return math.pi * self.radius * self.radius

    # determine if point is strictly inside circle
    def point_inside(self, p):
        return (self.center.dist(p) < self.radius)

    # determine if a circle is strictly inside this circle
    def circle_inside(self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

    # determine if a circle c intersects this circle (non-zero area of overlap)
    # the only argument c is a Circle object
    # returns a boolean
    def does_intersect(self, c):
        return self.center.dist(c.center) < (self.radius + c.radius)

    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    # the only argument, r, is a rectangle object
    def circle_circumscribes(self, r):
        rad = (1/2)* (r.ul).dist(r.lr)
        centertox = (r.ul.x + r.lr.x) / 2
        centertoy = (r.ul.y + r.lr.x) / 2
        return Circle(rad, centertox, centertoy)

    # string representation of a circle
    # takes no arguments and returns a string
    def __str__(self):
        return "Radius: " + str(self.radius) + ", Center: " + str(self.center)

    # test for equality of radius
    # the only argument, other, is a circle
    # returns a boolean
    def __eq__(self, other):
        tol = 1.0e-16
        return (abs(self.radius - other.radius) < tol)


class Rectangle(object):
    # constructor
    def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):
        if ((ul_x < lr_x) and (ul_y > lr_y)):
            self.ul = Point(ul_x, ul_y)
            self.lr = Point(lr_x, lr_y)
        else:
            self.ul = Point(0, 1)
            self.lr = Point(1, 0)

    # determine length of Rectangle (distance along the x axis)
    # takes no arguments, returns a float
    def length(self):
        return self.ul.x-self.lr.x



    # determine width of Rectangle (distance along the y axis)
    # takes no arguments, returns a float
    def width(self):
        return self.lr.y-self.lr.y

    # determine the perimeter
    # takes no arguments, returns a float
    def perimeter(self):
        return 2*((self.ul.x-self.lr.x)+(self.lr.y-self.lr.y))


    # determine the area
    # takes no arguments, returns a float
    def area(self):
        return (self.ul.x-self.lr.x)*(self.lr.y-self.lr.y)

    # determine if a point is strictly inside the Rectangle
    # takes a point object p as an argument, returns a boolean
    def point_inside(self, p):
        return self.ul.dist(p)

    # determine if another Rectangle is strictly inside this Rectangle
    # takes a rectangle object r as an argument, returns a boolean
    # should return False if self and r are equal
    def rectangle_inside(self, r):
        return ((r.ul.x - r.lr.x) < (self.ul.x - self.lr.x)) and ((r.ul.y - r.lr.y) < (self.ul.y - self.lr.y))

    # determine if two Rectangles overlap (non-zero area of overlap)
    # takes a rectangle object r as an argument returns a boolean
    def does_intersect(self, other):
        return (other.ul.x < self.ul.x < other.lr.x) and (other.lr.y < self.lr.y < other.ul.y)

    # determine the smallest rectangle that circumscribes a circle
    # sides of the rectangle are tangents to circle c
    # takes a circle object c as input and returns a rectangle object
    def rect_circumscribe(self, c):
        ul_x = c.center.x - (c.radius **2)
        ul_y = c.center.y - (c.radius **2)
        lr_x = c.center.x + (c.radius **2)
        lr_y = c.center.y + (c.radius **2)
        return Rectangle(ul_x, ul_y, lr_x, lr_y)

    # give string representation of a rectangle
    # takes no arguments, returns a string
    def __str__(self):
        return str(self.ul) + ';' + str(self.lr)

    # determine if two rectangles have the same length and width
    # takes a rectangle other as argument and returns a boolean
    def __eq__(self, other):
        tol = 1.0e-16
        return (abs(self.length() - other.length()) < tol) and (abs(self.width() - other.width()) < tol)


def main():
    # open the file geom.txt

    # create Point objects P and Q

    # print the coordinates of the points P and Q

    # find the distance between the points P and Q

    # create two Circle objects C and D

    # print C and D

    # compute the circumference of C

    # compute the area of D

    # determine if P is strictly inside C

    # determine if C is strictly inside D

    # determine if C and D intersect (non zero area of intersection)

    # determine if C and D are equal (have the same radius)

    # create two rectangle objects G and H

    # print the two rectangles G and H

    # determine the length of G (distance along x axis)

    # determine the width of H (distance along y axis)

    # determine the perimeter of G

    # determine the area of H

    # determine if point P is strictly inside rectangle G

    # determine if rectangle G is strictly inside rectangle H

    # determine if rectangles G and H overlap (non-zero area of overlap)

    # find the smallest circle that circumscribes rectangle G
    # goes through the four vertices of the rectangle

    # find the smallest rectangle that circumscribes circle D
    # all four sides of the rectangle are tangents to the circle

    # determine if the two rectangles have the same length and width

    # close the file geom.txt

    # This line above main is for grading purposes. It will not affect how
    # your code will run while you develop and test it.
    # DO NOT REMOVE THE LINE ABOVE MAIN

    in_file = open('geom.txt', 'r')

    coorp = (in_file.readline()).split()
    p = Point(float(coorp[0]), float(coorp[1]))

    coorq = (in_file.readline()).split()
    q = Point(float(coorq[0]),float(coorq[1]))

    print("Coordinates of P: "+str(p))
    print("Coordinates of Q: "+str(q))

    print("Distance between P and Q:"+str(p.dist(q)))
    coorc = (in_file.readline()).split()
    c = Circle(float(coorc[0]), float(coorc[1]),float(coorc[2]))

    coord = (in_file.readline()).split()
    d = Circle(float(coord[0]),float(coord[1]),float(coord[2]))
    print("Circle C: " + str(c))
    print("Circle D: " + str(d))
    print("Circumference of C: " + str(c.circumference()))
    print("Area of D: " + str(d.area()))
    print("P is", end=" ")
    if not (c.point_inside(p)):
        print("not", end=" ")
    print("inside C")
    print("C is", end=" ")
    if not (d.circle_inside(c)):
        print("not", end=" ")
    print("inside D")
    print("C does", end=" ")
    if not (d.does_intersect(c)):
        print("not", end=" ")
    print("intersect D")
    print("C is", end=" ")
    if c != d:
        print("not", end=" ")
    print("equal to D")

    coorg = (in_file.readline()).split()
    g = Rectangle(float(coorg[0]), float(coorg[1]), float(coorg[2]), float(coorg[3]))

    coorh = (in_file.readline()).split()
    h = Rectangle(float(coorh[0]), float(coorh[1]), float(coorh[2]), float(coorh[3]))

    print("Rectangle G: " + str(g))
    print("Rectangle H: " + str(h))
    print("Length of G: " + str(g.length()))
    print("Width of H: " + str(h.width()))
    print("Perimeter of G: " + str(g.perimeter()))
    print("Area of H: " + str(h.area()))

    print("P is", end=" ")
    if (not (g.point_inside(p))):
        print("not", end=" ")
    print("inside G")

    print("G is", end=" ")
    if (not (h.rectangle_inside(g))):
        print("not", end=" ")
    print("inside H")

    print("G does", end=" ")
    if (not (h.does_intersect(g))):
        print("not", end=" ")
    print("overlap H")

    smallcircle = Circle()
    print("Circle that circumscribes G: " + str(smallcircle.circle_circumscribes(g)))

    smallrectangle = Rectangle()
    print("Rectangle that circumscribes D: " + str(smallrectangle.rect_circumscribe(d)))

    print("Rectangle G is", end=" ")
    if (g != h):
        print("not", end=" ")
    print("equal to H")


    in_file.close()


\
if __name__ == "__main__":
    main()
