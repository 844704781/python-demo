file_path = './demo/test2'
try:
    with open(file_path, 'x', encoding='UTF-8') as file_obj:
        file_obj.write('周三')

except FileNotFoundError as e:
    print("文件未找到", e)
