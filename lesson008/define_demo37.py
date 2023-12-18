def make_averager():
    numbers = [1]
    print("外层id", id(numbers))

    def averager(n):
        nonlocal numbers
        print("内层1的id",id(numbers))
        numbers = numbers[:]
        print("内层2的id", id(numbers))
        return sum(numbers) / len(numbers)

    return averager


averager = make_averager()
# averager01 = make_averager()
print(averager(10))
