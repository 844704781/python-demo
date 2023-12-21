path = "./demo/test"
try:

    with open(path, encoding="UTF-8") as file_obj:
        content = ""
        while True:
            size = 6  # 每次读取的长度
            str = file_obj.read(size)

            if not str:
                break
            content += str

        print(content)
except FileNotFoundError as e:
    print("文件未找到", e)
