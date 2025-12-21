if __name__ == "__main__":
    pass

import line_module as lm

k1, b1 = lm.line_through_points(1, 2, 3, 6)
if k1 is None:
    print(f"Прямая через (1,2) и (3,6): x = {b1}")
else:
    print(f"Прямая через (1,2) и (3,6): y = {k1}*x + {b1}")

k2, b2 = lm.line_through_points(0, 0, 2, 4)
if k2 is None:
    print(f"Прямая через (0,0) и (2,4): x = {b2}")
else:
    print(f"Прямая через (0,0) и (2,4): y = {k2}*x + {b2}")

print("Прямые параллельны?", lm.are_parallel(k1, k2))

x, y = 2, 5
print(f"Точка ({x},{y}) на первой прямой?", lm.point_on_line(k1, b1, x, y))

x2, y2 = 2, 4
print(f"Точка ({x2},{y2}) на первой прямой?", lm.point_on_line(k1, b1, x2, y2))
