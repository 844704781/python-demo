## 基本语法

1. 在Python中严格区分大小写

   Java也是

   Node.js也是

2. Python中的每一行就是一条语句

   Java用;分号区分一条语句

   Node.js用;分号区分一条语句，也可以一行是一条语句

3. Python中每一行语句建议不要过长，每一行不超过80字符。

   如果一行语句需要超过80字符，建议多行书写，以\结尾换行

   在 Java 编码规范中，通常建议每行不要超过 80 到 120 个字符。

   Node.js 并没有强制规定每行代码的字符限制，通常，编码规范可能会建议每行不超过80到120个字符

4.  一条语句可以分多行书写，语句背后以\结尾

   ```python
   print('qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyui\
   opqwertyuiop')
   print('asdfgghhh')
   print(1+2+3\
         +5+\
         7)
   print(1+
         2
         +3)
   运行结果:
   qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop
   asdfgghhh
   18
   6
   ```
5.   Python是缩进严格的语言，所以在Python中不要随便写缩进

6.   注释
```text
Python
	用#表示单行注释，习惯#后面跟空格
	可以使用三个单引号 ''' 或三个双引号 """ 来创建多行注释

Java用// /**/ /****/表示注释

Javascript用// /**/ /****/表示注释
```

## 字面量和变量

字面量就是一个一个的值，比如1,2,3,4,5,6,'hello'

字面量所表示的意思就是它的字面的值，在程序中可以直接使用字面量

变量(variable)变量可以用来保存字面量，并且变量中保存的字面量是不定的

变量本身没有任何意思，它会根据不同的字面量表示不同的意思

一般我们在开发时，很少直接使用字面量，都是将字符保存到变量中，通过变量来引用字面量



## 变量和标识符

标识符
在Python中所有可以自主命名的内容都属于标识符
比如: 变量名、函数名、类名
标识符必须遵循标识符的命名规范

1. 标识符可以含有字母、数字、_,但不能使用数字开头
2. 标识符不能是Python中的关键字和保留字
       也不建议使用Python中的函数作为标识符，因为这样会导致函数被覆盖
3. 命名规范
   	在Python中注意遵循两种命名规范:
   		下划线命名法
   			所有字母小写，单词之间使用_分割
   			max_length min_length hello_world xxx_yyy_zzz
   		帕斯卡命名法（大驼峰命名法）
   			首字母大写，每个单词开头字母大写，其余字母小写
   			MaxLength MinLength HelloWorld XxxYyyZzz
   如果使用不符合标准的标识符，将会报错语法错误SyntaxError: invalid decimal literal



## 数据类型

