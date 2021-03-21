
import math

def paint_calc(height, width, cover):
    return math.ceil((width * height)/cover)

test_h = int(input("heigth of the wall: "))
test_w = int(input("width of the wall: "))
coverage = 5
number_of_cans = paint_calc(height=test_h, width=test_w, cover=coverage)
print(f"the number of cans of paint you'll need: {number_of_cans}")