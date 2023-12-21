path = "./demo/test"

try:
    with open(path, encoding="UTF-8") as file_obj:
        str = file_obj.read()
        print(str)
except FileNotFoundError as e:
    print("文件未找到", e)
