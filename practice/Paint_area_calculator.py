# program to calculate paint needed for the given area of the wall 
import math

test_h = int(input("Enter the Height of the wall: "))
test_w = int(input("Enter the width of the wall: "))

paint_coverage = 5 # 1 litre of paint can cover 5 sqr meter of wall

def paint_calc(height,width,coverage):
    area = height*width
    paint_needed = math.ceil(area/paint_coverage)
    print(f"{paint_needed} litre is needed for the wall  with {height}m height and {width}m width")

paint_calc(height=test_h, width=test_w, coverage=paint_coverage)