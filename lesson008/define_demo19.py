_map01 = {
    "a": 1,
    "b": 2,
    "c": 3
}

for a in _map01:
    print(a, _map01[a])

_keys = _map01.keys()
for a in _keys:
    print(a, _map01[a])

_values = _map01.values()
for a in _values:
    print(a)

_items = _map01.items()

for key, value in _items:
    print(key, value)

_list = [1, 2, 3]
