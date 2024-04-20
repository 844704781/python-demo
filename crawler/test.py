import execjs
import base64

# 创建一个JavaScript环境
context = execjs.compile("""
function add(a) {
    return a[0];
}
""")

# 调用JavaScript函数
result = context.call("add", ['hello'])
print(result)  # 输出：5
