s = {1, 2, 3} & {2, 3, 4}
print(s)  # {2, 3}
s = {1, 2, 3} | {2, 3, 4}
print(s)  # {1, 2, 3, 4}

s = {1, 2, 3, 4} - {2, 3}
print(s)  # {1, 4}

s = {1, 2, 3, 4} - {2, 3, 5}
print(s)  # {1, 4}

s = {1, 2, 3, 4} ^ {2, 3}
print(s)  # {1, 4}

s = {1, 2} < {1, 2, 3, 4}
print(s)  # True

s = {1, 2, 3, 4} < {1, 2, 3, 4}
print(s)  # False

s = {1, 2, 3, 4} >= {1, 2}
print(s)  # True
s = {1, 2, 3, 4} >= {1, 2, 3, 4}
print(s)  # True

s = {1, 2, 3, 4}
for value in s:
    print(value)


