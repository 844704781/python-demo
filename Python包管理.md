## powershell

### 设置代理

```shell
$ENV:ALL_PROXY ='http://127.0.0.1:7890'
```

https://pypi.org/project/pip/

## anaconda

与venv的区别主要是很方便安装和切换python版本

### conda的常用命令

#### 查看conda版本

```shell
conda --version
```

#### 创建环境

conda create -n [环境名] python=[python版本]

```shell
conda create -n conda_demo python=3.5
```



#### 激活环境

```shell
conda activate conda_demo
```

例子:

```text
(base) C:\Users\watermelon>activate conda_demo
激活成功后:
(conda_demo) C:\Users\watermelon>
```

#### 删除环境

```shell
conda remove -n conda_demo --all
```

####  反激活环境

```shell
conda deactivate
```

#### 查看有哪些虚拟环境

```shell
conda env list
```

比如:

```shell
(conda_demo) C:\Users\watermelon>conda env list
# conda environments:
#
base                     C:\Users\watermelon\anaconda3
conda_demo            *  C:\Users\watermelon\anaconda3\envs\conda_demo
data_visualization       C:\Users\watermelon\anaconda3\envs\data_visualization
```

#### 安装包

```shell
conda install django=2.0
```

#### 查看已经安装的包

```shell
conda list
```

#### 更新包

```shell
conda update django
```

#### 指定虚拟环境升级python

```shell
conda install python=3.12.2 -n media_crawler
```

#### 删除包

```shell
conda remove django
```

## pip包管理

python3.4版本以后，Python是自带pip的

### 查看pip版本

pip --version

```shell
watermelon@watermelon-win10:~$ pip --version
pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
```



### 升级pip版本

```shell
watermelon@watermelon-win10:~$ python -m pip install --upgrade pip
```



### 列出所有包

查看pip安装了哪些包

pip list

```shell
watermelon@watermelon-win10:~$ pip list
Package                Version
---------------------- -------------
blinker                1.4
command-not-found      0.3
cryptography           3.4.8
dbus-python            1.2.18
distro                 1.7.0
distro-info            1.1build1
gyp                    0.1
httplib2               0.20.2
importlib-metadata     4.6.4
jeepney                0.7.1
keyring                23.5.0
launchpadlib           1.10.16
lazr.restfulclient     0.14.4
lazr.uri               1.0.6
more-itertools         8.10.0
netifaces              0.11.0
oauthlib               3.2.0
pip                    22.0.2
PyGObject              3.42.1
PyJWT                  2.3.0
pyparsing              2.4.7
python-apt             2.4.0+ubuntu1
PyYAML                 5.4.1
SecretStorage          3.3.1
setuptools             59.6.0
six                    1.16.0
systemd-python         234
ubuntu-advantage-tools 8001
ufw                    0.36.1
unattended-upgrades    0.1
wadllib                1.3.6
wheel                  0.37.1
you-get                0.4.1650
zipp                   1.0.0
```

### 清空缓存信息

```shell
pip cache purge
```



### 安装

安装最新版本的包

pip install 包名

指定版本号安装包:

pip install "request==2.18.0"

```shell
watermelon@watermelon-win10:~$ pip install requests
```



#### 使用阿里云源安装

```shell
pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
```



### 移除

pip uninstall 包名

```shell
watermelon@watermelon-win10:~$ pip uninstall requests
```

### 升级包

pip install --upgrade 包名

```shell
watermelon@watermelon-win10:~$ pip install --upgrade requests
```







### 生成requirments.txt

注意:一般是在虚拟环境中生成

pip freeze相当于把pip list里的包按照requirements.txt的格式展示出来

```shell
watermelon@watermelon-win10:~$ pip freeze > requirments.txt
```

### 使用requirement.txt

```shell
watermelon@watermelon-win10:~$ pip install -r requirments.txt
```



## 虚拟环境

创建一个或多个目标目录中的虚拟Python环境。



### 查看venv所有命令

```
python -m venv -h
```

```shell
位置参数：

ENV_DIR：要在其中创建环境的目录。
选项：

-h, --help：显示帮助消息并退出。
--system-site-packages：允许虚拟环境访问系统site-packages目录。
--symlinks：尝试在平台默认不是符号链接的情况下使用符号链接而不是复制。
--copies：尝试使用复制而不是符号链接，即使符号链接是平台默认的情况。
--clear：在创建环境之前，如果环境目录已经存在，则删除其内容。
--upgrade：假定Python已经在原地升级，将环境目录升级为使用此版本的Python。
--without-pip：跳过在虚拟环境中安装或升级pip（默认情况下通过引导安装pip）。
--prompt PROMPT：为此环境提供替代的提示前缀。
--upgrade-deps：升级核心依赖项：将pip和setuptools升级到PyPI中的最新版本。
创建环境后，您可能希望激活它，例如通过在其bin目录中引用激活脚本。
```
### 创建虚拟环境

```shell
python -m venv venvdemo
```



Include:几乎是空的，平时不关注

Lib目录

Script目录

```shell
├── Activate.ps1 激活，powershell用的激活文件
├── activate 激活，根据环境自己选择激活文件
├── activate.bat  激活，cmd用的激活文件
├── deactivate.bat 反激活
├── pip.exe
├── pip3.12.exe
├── pip3.exe
├── python.exe
└── pythonw.exe
```



### 激活虚拟环境

windows激活:

```shell
cd venvdemo\Scripts
./activate
```

ubuntu激活:

```shell
source venvdemo/bin/activate
```



虚拟环境的系统路径

```shell
>>> import sys
>>> from pprint import pprint
>>> pprint(sys.path)
['',
 'C:\\Python312\\python312.zip',
 'C:\\Python312\\DLLs',
 'C:\\Python312\\Lib',
 'C:\\Python312',
 'C:\\Users\\watermelon\\workspace\\venv_test\\venvdemo',
 'C:\\Users\\watermelon\\workspace\\venv_test\\venvdemo\\Lib\\site-packages']
```



正式环境的系统路径

```shell
>>> import sys
>>> from pprint import pprint
>>> pprint(sys.path)
['',
 'C:\\Python312\\python312.zip',
 'C:\\Python312\\DLLs',
 'C:\\Python312\\Lib',
 'C:\\Python312',
 'C:\\Users\\watermelon\\AppData\\Roaming\\Python\\Python312\\site-packages',
 'C:\\Python312\\Lib\\site-packages']
```



虚拟环境的环境变量

```shell
$env:PATH

C:\Users\watermelon\workspace\venv_test\venvdemo\Scripts;c:\Users\watermelon\AppData\Local\Programs\cursor\resources\app\bin;C:\Python312\Scripts\;C:\Python312\;C:\Python27\;C:\Python27\Scripts;C:\Program Files\AdoptOpenJDK\jdk-8.0.292.10-hotspot\bin;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;C:\Program Files\NVIDIA Corporation\NVIDIA NvDLISR;C:\ProgramData\chocolatey\bin;C:\Users\watermelon\AppData\Roaming\nvm;C:\Program Files\nodejs;C:\ProgramData\chocolatey\lib\maven\apache-maven-3.9.2\bin;C:\Program Files\Git\cmd;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files (x86)\Tencent\微信web开发者工具\dll;C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\;C:\Users\watermelon\AppData\Local\Microsoft\WindowsApps;C:\Users\watermelon\AppData\Local\JetBrains\Toolbox\scripts;C:\Users\watermelon\AppData\Roaming\nvm;C:\Program Files\n;C:\Users\watermelon\AppData\Local\Microsoft\WindowsApps;C:\Users\watermelon\AppData\Local\JetBrains\Toolbox\scripts;C:\Users\watermelon\AppData\Roaming\nvm;C:\Program Files\nodejs;C:\Users\watermelon\AppData\Local\Microsoft\WindowsApps;;C:\Users\watermelon\AppData\Local\Programs\Fiddler;C:\ProgramData\mingw64\mingw64\bin;
```



正式环境的环境变量

```shell
$env:PATH

c:\Users\watermelon\AppData\Local\Programs\cursor\resources\app\bin;C:\Python312\Scripts\;C:\Python312\;C:\Python27\;C:\Python27\Scripts;C:\Program Files\AdoptOpenJDK\jdk-8.0.292.10-hotspot\bin;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;C:\Program Files\NVIDIA Corporation\NVIDIA NvDLISR;C:\ProgramData\chocolatey\bin;C:\Users\watermelon\AppData\Roaming\nvm;C:\Program Files\nodejs;C:\ProgramData\chocolatey\lib\maven\apache-maven-3.9.2\bin;C:\Program Files\Git\cmd;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files (x86)\Tencent\微信web开发者工具\dll;C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\;C:\Users\watermelon\AppData\Local\Microsoft\WindowsApps;C:\Users\watermelon\AppData\Local\JetBrains\Toolbox\scripts;C:\Users\watermelon\AppData\Roaming\nvm;C:\Program Files\n;C:\Users\watermelon\AppData\Local\Microsoft\WindowsApps;C:\Users\watermelon\AppData\Local\JetBrains\Toolbox\scripts;C:\Users\watermelon\AppData\Roaming\nvm;C:\Program Files\nodejs;C:\Users\watermelon\AppData\Local\Microsoft\WindowsApps;;C:\Users\watermelon\AppData\Local\Programs\Fiddler;C:\ProgramData\mingw64\mingw64\bin;
```



由上可知，标准库用的都是C:\\Python312\\Lib

虚拟环境只是把环境变量增加了C:\Users\watermelon\workspace\venv_test\venvdemo\Scripts;

由于环境变量的优先级，所以当前目录使用的python.ext与pip.ext都是该目录中的





### 退出虚拟环境

```shell
    deactivate
```





### IDE中使用虚拟环境

只要指定interpreter的路径为虚拟环境python的路径即可



### 复制虚拟环境

```shell
cd venvdemo\Scripts
./activate
pip freeze > requirments.txt
pip install -r requirments.txt
```







## 总结

创建项目的步骤

```shell
mkdir myproject
python -m venv .venv
cd .venv/bin/
source activate
cd ../../
pip install xxx -i xxxxx
pip list
pip freeze > requirements.txt
pip install -r requirements.txt -i xxx
```

安装python的步骤

```shell
1. 安装anaconda软件，可以图形化，也可以命令行
2. conda create -n conda_demo python=3.8 
3. conda activate conda_demo
```

