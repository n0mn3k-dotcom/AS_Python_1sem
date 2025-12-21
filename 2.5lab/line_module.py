def line_equation(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "x = " + str(x1)
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    return f"y = {k}*x + {b}"

def are_parallel(k1, b1, k2, b2):
    return k1 == k2

def is_point_on_line(x0, y0, k, b):
    return y0 == k * x0 + b
