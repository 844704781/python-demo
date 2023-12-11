from time import *

start = time()
i = 1
while i <= 20000:
    j = 1
    _count = 0
    while j <= (i**0.5):
        if (i % j) == 0:
            _count += 1
            if _count >2:
                break
        j = j + 1
    if _count == 2:
        pass
    i = i + 1
end = time()
print(end - start)