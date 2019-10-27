from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    rectangle = Rectangle(3, 2, "black")
    square = Square(5, "red")
    circle = Circle(5, "green")
    print(rectangle)
    print(square)
    print(circle)

if __name__ == "__main__":
    main()