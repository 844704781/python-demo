file_path = '/Users/watermelon/Pictures/ia2ibo3dorcypsypokix56gcbmkhon6z.jpeg'
file_path1 = './demo/test1.jpeg'
try:
    with open(file_path, 'rb') as file_obj:

        with open(file_path1, 'wb') as write_obj:
            chunk = 1024 * 100
            while True:
                content = file_obj.read(1)
                if not content:
                    print("写完了")
                    break
                write_obj.write(content)

except FileNotFoundError as e:
    print("文件未找到", e)
