from time import *

start = time()
num = 2
while num <= 1000000:
    if num != 2 and num % 2 == 0:
        num = num + 1
        continue
    # 3
    j = 1
    _count = 0
    while j <= (num**0.5):
        if(num % j) == 0:
            _count += 1
            if _count >1:
                break
        j = j + 1
    if _count == 1:
        pass

    num = num + 1
end = time()
print(end - start)
#100w 18.14235520362854
#100w 17.383357763290405
#100w