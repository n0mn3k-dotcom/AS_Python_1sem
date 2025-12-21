def line_through_points(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return None, x1
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k*x1
    return k, b

def are_parallel(k1, k2):
    if k1 is None and k2 is None:
        return True
    if k1 is None or k2 is None:
        return False
    return k1 == k2

def point_on_line(k, b, x, y):
    if k is None:
        return x == b
    return y == k*x + b
