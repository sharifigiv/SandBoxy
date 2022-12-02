from math import *
from numpy import dot
from sympy import numbered_symbols

class Vec2 ():
    def __init__(self, X, Y):
        Vec2.x = X
        Vec2.y = Y

    def lenght (self):
        return sqrt(Vec2.x * Vec2.x + Vec2.y * Vec2.y)

    def add (self, vec):
        return Vec2(vec.x + Vec2.x, vec.y + Vec2.y)

    def minus (self, vec):
        return Vec2(Vec2.x - vec.x, Vec2.y - vec.y)

    def subtract (self, vec):
        return Vec2(Vec2.x - vec.x, Vec2.y - vec.y)

    def multiply (self, num):
        return Vec2(num * Vec2.x, num * Vec2.y)

    def division (self, num):
        return Vec2(Vec2.x / num, Vec2.y / num)

    def scale (self, n):
        return Vec2(Vec2.x * n, Vec2.y * n)

    def dot (self, vec):
        return Vec2(Vec2.x * vec.x, Vec2.y * vec.y)

    def cross (self, vec):
        return (Vec2.x * vec.y - Vec2.y * vec.x)

    def rotate (self, center, angle):
        # Rotate in counterclockwise

        r = []
        x = Vec2.x - center.x
        y = Vec2.y - center.y

        r.append(x * cos(angle) - y * sin(angle))
        r.append(x * sin(angle) + y * cos(angle))
        r[0] += center.x
        r[1] += center.y

        return Vec2(r[0], r[1])

    def normalize (self):
        len = Vec2.lenght()

        if (len > 0):
            len = 1 / len

        return Vec2(Vec2.x * len, Vec2.y * len)

    def distance (self, vec):
        x = Vec2.x - vec.x
        y = Vec2.y - vec.x

        return sqrt(x * x + y * y)

def DotProduct (A, B):
    return dot(A, B)