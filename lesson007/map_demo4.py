a = {"a": 1, "b": "2"}
b = a.copy()
print(id(a), a)  # 2130285378624 {'a': 1, 'b': '2'}
print(id(b), b)  # 2130285471936 {'a': 1, 'b': '2'}
a['a'] = 23
# 经过复制后对象是独立的，修改一个不会影响另一个
print(a)  # {'a': 23, 'b': '2'}
print(b)  # {'a': 1, 'b': '2'}

order1 = {
    "total": 100,
    "commodity": [{
        "name": "衬衫",
        "unit_price": 51
    }, {
        "name": "裤子",
        "unit_price": 49
    }]
}
order2 = order1.copy()
order1['commodity'][0]['name'] = '毛衣'
print(order1['commodity'])
print(order2['commodity'])

d1 = {'a': {'name': '孙悟空', 'age': 10}, 'b': 2, 'c': 3}
d2 = d1.copy()
d1['a']['name'] = '猪八戒'
print(d1)  # {'a': {'name': '猪八戒', 'age': 10}, 'b': 2, 'c': 3}
print(d2)  # {'a': {'name': '猪八戒', 'age': 10}, 'b': 2, 'c': 3}
