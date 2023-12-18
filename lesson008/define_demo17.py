a = 10
b = 20


def fn1():
    c = 10
    fun1_locals = locals() #获取函数命名空间
    print(fun1_locals)  # {'c': 10}
    _global = globals()
    print(_global)
    '''
    {  
    '__name__': '__main__',  
    '__doc__': None,  
    '__package__': None,  
    '__loader__':<_frozen_importlib_external.SourceFileLoader object at 0x00000266EC19BB30>,  
    '__spec__': None,  
    '__annotations__': {},  
    '__builtins__': <module 'builtins' (built-in)>,  
    '__file__': 'C:\\Users\\watermelon\\workspace\\python-lesson\\lesson008\\define_demo17.py',  
    '__cached__': None,  
    'a': 10,  
    'b': 20,  
    'fn1': <function fn1 at 0x00000266EC33BCE0>  
}
    '''

fn1()
