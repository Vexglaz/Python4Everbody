#Polygon Area Calculator

from turtle import width


class Rectange:
    name = ""

    def __init__(self, width = 1, height = 1):
        self.wid = width
        self.het = height
        self.name = "Rectangle(width="+str(self.wid)+", height="+str(self.het)+")"
    def set_width(self, WD):
        self.wid = WD
        self.name = "Rectangle(width="+str(self.wid)+", height="+str(self.het)+")"
        return self.wid
    def set_height(self, hei):
        self.het = hei
        self.name = "Rectangle(width="+str(self.wid)+", height="+str(self.het)+")"
        return self.het
    def get_area(self):
        area = self.wid * self.het
        return area
    def get_perimeter(self):
        perimeter = (2*self.wid) + (2*self.het)
        return perimeter
    def get_diagonal(self):
        diagonal = ((self.wid**2 + self.het**2)**.5)
        return diagonal
    def get_picture(self):
        x = self.wid
        y = self.het
        line = ""
        if(x > 50 or y > 50):
            return print("Too big for picture.")
        for i in range(y):
            for j in range(x):
                line = line + "*"
            line = line + "\n"
        return print(line)
    def get_amount_inside(self, shape):
        w2 = shape.wid
        h2 = shape.het
        fit = self.wid * self.het / (w2 * h2)
        return fit

class Square(Rectange):
    def __init__(self, length = 1):
        self.wid = length
        self.het = length
        self.name = "Square(side="+str(self.het)+")"
    def set_height(self, hei):
        self.wid = hei
        self.het = hei
        self.name = "Square(side="+str(self.het)+")"
        return self.het
    def set_width(self, WD):
        self.wid = WD
        self.het = WD
        self.name = "Square(side="+str(self.het)+")"
        return self.het
    

rect = Rectange(10,5)
rect.set_height(3)
print(rect.get_picture())

sq = Square(9)
print(sq.get_diagonal())
print(sq.get_picture())
sq.set_height(4)

rect.set_height(8)
rect.set_width(16)

print(rect.get_amount_inside(sq))