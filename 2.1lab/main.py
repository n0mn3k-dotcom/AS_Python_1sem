if __name__ == "__main__":
    pass

def check_keys(d, keys):
    for k in keys:
        if k not in d:
            return False
    return True


d = {1: 2, 3: 4}
keys = [1, 3]

print(check_keys(d, keys))
