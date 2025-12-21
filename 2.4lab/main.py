if __name__ == "__main__":
    pass



#а)
def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b

print(calculate(10, 5))
print(calculate(10, 5, operation="multiply"))

#б)
def modify_strings(strings, case=None):
    result = []

    if case == "upper":
        for s in strings:
            result.append(s.upper())
        return result

    if case == "lower":
        for s in strings:
            result.append(s.lower())
        return result

    return strings

print(modify_strings(["Hello", "World"]))
print(modify_strings(["Hello", "World"], case="upper"))

#в)
def average(*nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)

print(average(1, 2, 3, 4, 5))
print(average(10, 20))

#г)
def merge_dictionaries(main_dict, **dicts):
    result = main_dict.copy()
    for d in dicts.values():
        for key in d:
            result[key] = d[key]
    return result

print(merge_dictionaries({'a': 1, 'b': 2}, dict1={'b': 3, 'c': 4}))
print(merge_dictionaries({'x': 5}, dict1={'y': 6}, dict2={'z': 7}))
