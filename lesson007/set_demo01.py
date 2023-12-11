s = {4, 2, 1, '2', 2, 'hello', 'cxk'}
print(s, type(s))  # {1, 2, 'cxk', 4, 'hello', '2'} <class 'set'>
s = {}
print(type(s))  # <class 'dict'>

s = set()
print(s, type(s))  # set() <class 'set'>
# 转换序列
s = set([1, 23, 1, 5, 7, 1, 34, 23])
print(s)  # {1, 34, 5, 7, 23}

s = set('hello world')  # {'e', 'd', 'r', ' ', 'o', 'l', 'w', 'h'}
print(s)

# 转换字典
s = set({
    'a': 1,
    'b': 2,
    'a': 3
})
print(s)  # {'a', 'b'}

s = {4, 2, 1, '2', 2, 'hello', 'cxk'}
print(4 in s)  # True
print(2 not in s)  # False

s = {4, 2, 1, '2', 2, 'hello', 'cxk'}
print(len(s))  # 6

s = set()
s.add(1)
print(s)  # {1}
print(s)

# 合并序列
s = set('hello')
s.update('world')
print(s)  # {'o', 'l', 'd', 'r', 'h', 'w', 'e'}
# 合并集合
s1 = {1, 1, 1, 3}
s2 = {2, 2, 2, 1}
s1.update(s2)
print(s1)  # {1, 2, 3}
print(s2)  # {1, 2}
# 合并字典
s1 = set('hello')
s1.update({'a': 'world'})
print(s1)  # {'h', 'e', 'o', 'l', 'a'}
# 合并集合
s1 = set('hello')
s1.update(set('world'))
print(s1)  # {'h', 'o', 'e', 'r', 'l', 'd', 'w'}

s = {4, 2, 1, '2', 2, 'hello', 'cxk'}
print(s)  # {1, 2, 'hello', 4, 'cxk', '2'}
s.pop()
# 看似删除了集合中的第一个，但是我们并不知
# 道集合的顺序是怎么排的，这是编译器按照他
# 的规则自己排的，所以我们认为是随机删的
print(s)  # {2, 'hello', 4, 'cxk', '2'}

s = {4, 2, 1, '2', 2, 'hello', 'cxk'}
s.remove('cxk')
print(s)  # {1, 2, 4, '2', 'hello'}

s = {4, 2, 1, '2', 2, 'hello', 'cxk'}
s.clear()
print(s)  # set()

s = {(1, 2), 'a'}  # TypeError: unhashable type: 'set'
s = s.copy()
