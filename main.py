from math_painter.canvas import Canvas
from shapes import Rectangle, Square

canvas_width = int(input('Input canvas width: '))
canvas_height = int(input('Input canvas height: '))
color_options = {"black": (0, 0, 0), "white": (255, 255, 255)}
color_input = input("Chooses colors, black or white: ")

canvas = Canvas(width=canvas_width, height=canvas_height, color=color_options[color_input])

while True:
    shape_type = input('What would you like to draw? Enter quit to quit.')
    if shape_type.lower() == 'rectangle':
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter width of the rectangle: "))
        rec_height = int(input("Enter height of the rectangle: "))
        red = int(input("How much red should the rectangle have: "))
        green = int(input("How much green: "))
        blue = int(input("Hoe much blue: "))

        # Create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, width=rec_width, height=rec_height, color=(red, green, blue))
        r1.draw(canvas)

    if shape_type.lower() == 'square':
        sqr_x = int(input("Enter x of the square: "))
        sqr_y = int(input("Enter y of the square: "))
        sqr_side = int(input("Enter the side length of the square: "))
        red = int(input("How much red should the square have: "))
        green = int(input("How much green: "))
        blue = int(input("Hoe much blue: "))

        # Create the rectangle
        s1 = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red, green, blue))
        s1.draw(canvas)

    if shape_type.lower() == 'quit':
        break


canvas.make('canvas.png')




