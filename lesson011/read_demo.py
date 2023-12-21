path = "./demo/test"
r = open(path, encoding="UTF-8")
str = r.read()
print(str)  # hello world
r.close()
