'''
创建一个函数，用来检查一个任意的字符串是否是回文字符串，如果是返回True，否则返回False

回文字符串，字符串从前往后念和从后往前念是一样的
0 -1   abcdefgfedcba
0 -1   bcdefgfedcb
0 -1   cdefgfedc
0 -1   defgfed
0 -1   efgfe
0 -1   fgf
   g

结束条件:
    len(str)<2
    f(0)!=f(-1)
'''


def palindrome(_str):
    '''
    递归条件:
        fn(_str[1:-1])
    结束条件:
        len(_str) < 2
        _str[0] != _str[-1]
    '''
    if len(_str) < 2:
        return True
    if _str[0] != _str[-1]:
        return False
    else:
        return palindrome(_str[1:-1])

print(palindrome("abcdefgfedcba"))
