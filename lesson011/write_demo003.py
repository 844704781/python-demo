file_path = './demo/test'
try:
    with open(file_path, 'w', encoding="UTF-8") as write_obj:
        write_obj.write("123456789\n")
        write_obj.write("abcdefghi\n")
        write_obj.write("qwertyuio\n")
        write_obj.write("asdfghjkl\n")
        write_obj.write("zxcvbnm,.\n")

    with open(file_path, 'rb') as read_obj:
        content = read_obj.read()   
        print(content)
        read_obj.seek(9)
        read_obj.seek(-10, 2)  # 从结尾位置向前读10位
        content = read_obj.read()
        print(content)  # b'zxcvbnm,.\n'
except FileNotFoundError as e:
    print("文件未找到", e)
