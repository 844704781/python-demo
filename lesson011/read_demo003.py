path = "./demo/test"
try:

    with open(path, encoding="UTF-8") as file_obj:
        for i in file_obj:
            print(i)
except FileNotFoundError as e:
    print("文件未找到", e)
