from PIL import Image
from math import factorial
from colorsys import hsv_to_rgb

def get_color(value, minimum, maximum, hsv_constant=120):
    h = (float(value-minimum) / (maximum-minimum)) * hsv_constant
    r,g,b = hsv_to_rgb(h/360, 1., 1.)
    return (int(r*255), int(g*255), int(b*255))

def pascal_triangle(no_of_rows, modulo):
    image = Image.new('RGB', size=(no_of_rows*2, no_of_rows*2))
    for count in range(no_of_rows):
        last_x = -count
        for element in range(count + 1): 
            if element:
                last_x += 2
            else:
                last_x += no_of_rows-1
            item = int(factorial(count)/(factorial(element) * factorial(count - element))) % modulo
            color = get_color(item, 0, modulo-1)
            image.putpixel((last_x, count), color)
            image.putpixel((last_x+1, count), color)
    image.save('pascal.png')
            