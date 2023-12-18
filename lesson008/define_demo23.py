def generate_combinations_iterative(elements, k):
    n = len(elements)
    if k > n or k < 0:
        return []

    combinations = []
    indices = list(range(k))

    while indices[0] < n - k + 1:
        combination = [elements[i] for i in indices]
        combinations.append(combination)

        i = k - 1
        while i >= 0 and indices[i] == i + n - k:
            i -= 1

        if i == -1:
            break

        indices[i] += 1
        for j in range(i + 1, k):
            indices[j] = indices[j - 1] + 1

    return combinations


# 示例使用
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 5
result = generate_combinations_iterative(elements, k)
print(result)
