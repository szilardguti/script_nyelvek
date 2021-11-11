#!/usr/bin/env python3


class Sphere:
    def __init__(self, x, y, z, r):
        self.center_x = x
        self.center_y = y    
        self.center_z = z
        self.radius = r
        

    def relocate(self, x, y, z):
        self.center_x = x
        self.center_y = y    
        self.center_z = z
        
        
    def resize(self, new_r):
        self.radius = new_r
        
    
    def area(self):
        return (4 * 3.14 * self.radius**3)/3
        
        
    def __lt__(self, other_sphere):
        return self.area() < other_sphere.area()
        
        
    def __le__(self, other_sphere):
        return self.area() <= other_sphere.area()
        
        
    def __gt__(self, other_sphere):
        return self.area() > other_sphere.area()
        
        
    def __ge__(self, other_sphere):
        return self.area() >= other_sphere.area()
        
        
    def __str__(self):
        return "Középpont: " + str((self.center_x, self.center_y, self.center_z)) + " rádiusz: " + str(self.radius)
        

def main():
    s = Sphere(0, 0, 0, 5)
    s.relocate(1,1,5)
    print(s)
    
    s2 = Sphere(0, 2, 3, 10)
    print(s > s2)
    print(s < s2)
    s2.resize(5)
    print(s >= s2)

if __name__ == "__main__":
    main()
