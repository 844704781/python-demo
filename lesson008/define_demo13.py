def fn(a: str, b: int, c: bool) -> float:
    '''
    这是一个文档字符串的示例
    :param a: 作用xxx
    :param b: 作用xxx
    :param c: 作用xxx
    :return: 返回值
    '''

    return 10


help(fn)
'''
fn(a: str, b: int, c: bool) -> float
    这是一个文档字符串的示例
    :param a: 作用xxx
    :param b: 作用xxx
    :param c: 作用xxx
    :return: 返回值
'''

help(print)
'''
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.
'''
