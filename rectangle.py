class Rectangle:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b

    def is_valid(self) -> bool:
        """
        This method checks if the rectangle is valid
        
        Args:
            No
        Returns: 
            bool: True if the rectangle is valid, False otherwise
        """ 
        if self.a<0 or self.b<0:
            return False
        else:
            return True

    def perimeter(self):
        """
        This method finds the perimeter of the rectangle.
        Args:
            No
        Returns:
            float or int: return perimeter of the rectangle if the rectangle is valid, 0 otherwise
        """
        if self.a<0 or self.b<0:
            return 0
        else:
            return (self.a + self.b)*2

    def area(self) -> float:
        """
        This method finds the area of the rectangle.
        Args:
            No
        Returns:
            float or int:  return area of the rectangle if the rectangle is valid, 0 otherwise 
        """
        if self.a<0 or self.b<0:
            return 0
        else:
            return self.a*self.b

    

x=Rectangle(10.0, 2.0)
print(x.area())

# Tugadi