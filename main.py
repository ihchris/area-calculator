import math

# Importing necessary modules

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return math.pi * radius ** 2

# Function to calculate the volume of a sphere
def calculate_sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

# Function to calculate the factorial of a number
def calculate_factorial(num):
    if num == 0:
        return 1
    else:
        return num * calculate_factorial(num - 1)

# Main program
if __name__ == "__main__":
    # Get user input
    radius = float(input("Enter the radius: "))
    num = int(input("Enter a number: "))

    # Calculate and display the area of a circle
    circle_area = calculate_circle_area(radius)
    print("The area of the circle is:", circle_area)

    # Calculate and display the volume of a sphere
    sphere_volume = calculate_sphere_volume(radius)
    print("The volume of the sphere is:", sphere_volume)

    # Calculate and display the factorial of a number
    factorial = calculate_factorial(num)
    print("The factorial of", num, "is:", factorial)