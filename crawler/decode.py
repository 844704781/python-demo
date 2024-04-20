import execjs
import json


def run_js_code(js_code, data, buffer):
    ctx = execjs.compile(js_code)
    test = ctx.call('my_decode', data, buffer)
    return test


def decode(data, buffer):
    with open('./decode.js', 'r') as file:
        js_code = file.read()

    # 将 data 转换为 JavaScript 中可识别的数据类型

    return run_js_code(js_code, data, buffer)


with open('./data') as file:
    data = json.loads(file.read())
    print(data)

with open('./buffer') as file:
    buffer = json.loads(file.read())
    print(buffer)

# 示例
result = decode(data, buffer)
print(result)
