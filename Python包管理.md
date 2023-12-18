## pip包管理

python3.4版本以后，Python是自带pip的

### 查看pip版本

pip --version

```shell
watermelon@watermelon-win10:~$ pip --version
pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
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

### 安装

安装最新版本的包

pip install 包名

指定版本号安装包:

pip install "request==2.18.0"

```shell
watermelon@watermelon-win10:~$ pip install requests
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



## 虚拟环境

