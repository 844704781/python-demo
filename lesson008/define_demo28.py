'''
创建一个函数，用来检查一个任意的字符串是否是回文字符串，如果是返回True，否则返回False

回文字符串，字符串从前往后念和从后往前念是一样的
   abcba
递归公式：
abcba
0,4
1,3
2,2
abccba:
0,5
1,4
2,3
fn(words,n)

结束条件:
    n> = len-1-n:
        return True
    words[start] != words[end]
        return False
'''


def palindrome(_str):
    def is_equals(words, n):
        end = len(words) - 1 - n
        if n >= end:
            return True
        if words[n] != words[end]:
            return False
        return is_equals(words, n + 1)

    _words = list(_str)
    return is_equals(_words, 0)


print(palindrome('abcba'))
