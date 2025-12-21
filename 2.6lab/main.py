if __name__ == "__main__":
    pass

import line_module as lm


eq1 = lm.line_equation(1, 2, 3, 6)
print("Уравнение прямой через (1,2) и (3,6):", eq1)


parallel = lm.are_parallel(2, 1, 2, 3)
print("Прямые параллельны?", parallel)


on_line = lm.is_point_on_line(2, 5, 2, 1)
print("Точка (2,5) на прямой y=2*x+1?", on_line)
