if __name__ == "__main__":
    pass

# a
def check_keys(d, keys):
    for k in keys:
        if k not in d:
            return False
    return True


d = {1: 2, 3: 4}
keys = [1, 3]

print(check_keys(d, keys))

#б

def comb_bukv(d, key):
    result = []

    if key not in d:
        return result

    s = d[key]

    for i in range(len(s)):
        for j in range(len(s)):
            for k in range(len(s)):
                if i != j and i != k and j != k:
                    result.append(s[i] + s[j] + s[k])

    return result


d = {1: 'abc'}
print(comb_bukv(d, 1))

#в

def avg_dict(d):
    new_dict = {}

    for key in d:
        s = d[key]
        summa = 0

        for x in s:
            summa += x

        avg = round(summa / len(s), 1)
        new_dict[key] = avg

    return new_dict


d = {1: [2, 3, 4], 3: [5, 6, 7], 5: [8, 9, 0]}
print(avg_dict(d))



