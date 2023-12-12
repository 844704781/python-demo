def print_value(a):
    print("a_id:", id(a))
    a = 1
    print("a_id:", id(a))



b = 1
print("b id:", id(b))
b = 2
print("b id:", id(b))
print_value(b)
print("b id:", id(b))