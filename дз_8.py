result = []
def divider(a, b):
    if a < b:
        raise ValueError("a менше b")
    if b > 100:
        raise IndexError("b більше за 100")
    return a / b
data = {10: 2, 2: 5, "123": 4, 18: 0, 1: 15, 8: 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError as ve:
        print(f"ValueError для ключа {key}: {ve}")
    except IndexError as ie:
        print(f"IndexError для ключа {key}: {ie}")
    except Exception as e:
        print(f"Інший виняток для ключа {key}: {e}")
print(result)
