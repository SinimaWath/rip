from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square

def main():
    rectangle = Rectangle(3, 2, "black")
    square = Square(5, "red")
    print(rectangle)
    print(square)

if __name__ == "__main__":
    main()