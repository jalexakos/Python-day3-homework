from math import pi

def house_footage():
    length = input("What is the length?: ")
    width = input("What is the width?: ")
    area = int(length) * int(width)
    print(f"The square footage of the house is: {area} feet.")
    return area

def circle_circ():
    radius = input("What is the radius of the circle?: ")
    circumference = 2 * pi * int(radius)
    print(f"The circumference of the circle is: {circumference}.")
    return circumference