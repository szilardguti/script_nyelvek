#!/usr/bin/env python3
    
    
class Hello:
    """
        This is my docstring
    """
    def create_name(self, name):
        self.name = name #nem kell külön deklarálni!    
    
    
    def display_name(self):
        return self.name

    
    def greet(self):
        print(f"Hello {self.name}!")
        

def main():
    h = Hello()
    h.create_name("Alice")
    print(h.display_name())
    h.greet()
    

if __name__ == "__main__":
    main()
