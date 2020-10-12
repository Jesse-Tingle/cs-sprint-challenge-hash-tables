def intersection(arrays):
    result = []
    num_cache = {}
    for ele in arrays:
        for num in ele:
            if num not in num_cache:
                num_cache[num] = 0
            num_cache[num] += 1

    for k, v in num_cache.items():
        if v == len(arrays):
            result.append(k)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
