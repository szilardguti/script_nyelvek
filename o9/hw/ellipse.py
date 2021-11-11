#!/usr/bin/env python3


class Ellipse:
    def __init__(self, major_axis, minor_axis):
        if minor_axis > major_axis:
            major_axis, minor_axis = minor_axis, major_axis
        self.major_axis = major_axis
        self.minor_axis = minor_axis
        
        
    def area(self):
        return (self.major_axis/2) * (self.minor_axis/2) * 3.14


    def __str__(self):
        return "Ellipse({major},{minor})".format(major = self.major_axis, minor = self.minor_axis)
        

def main():
    e = Ellipse(12, 10)
    print("{Ellipse} Area: {area}".format(Ellipse = e, area = e.area()))

    circle = Ellipse(24, 24)
    print(circle.area())
    
    w = Ellipse(1, 23)
    print(w.area())
    

if __name__ == "__main__":
    main()
