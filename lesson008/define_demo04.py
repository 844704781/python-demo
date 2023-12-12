def speak(obj):
    print("id:", id(obj))
    print("type:", type(obj))
    print("value:", obj)
    print("-" * 20)


# 整数
speak(1)
'''
id: 4394055984
type: <class 'int'>
value: 1
'''
# 浮点
_f = 1.11
speak(1.11)
'''
id: 4394742736
type: <class 'float'>
value: 1.11
'''
# bool
speak(True)
'''
id: 4400375056
type: <class 'bool'>
value: True
'''
# str
speak("hello")
'''
id: 4396129648
type: <class 'str'>
value: hello
'''
# None
speak(None)
'''
id: 4400454608
type: <class 'NoneType'>
value: None
'''


def speak(obj):
    obj(1, 2)

def add(i, j):
    print(f"{i}+{j}=", i + j)

speak(add)
'''
1+2= 3
'''
