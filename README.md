# cmds
=========================================

##  功能说明
```
用python执行操作系统bash命令
```

## 安装方法
```
1）源码安装：
git clone https://github.com/qiueer/cmds
cd cmds
python setup.py install
2）pip安装
pip install cmds
```

## 使用示例
```
    >>> from cmds import cmds
    >>> cmds('ls . | grep ".pyc"')
    cmds.pyc
```

```
    >>> cmds('ls . ').cmds('grep ".pyc"')
    cmds.pyc
```

## 注意
```
此py包不适宜执行不受信任的命令，见：
<https://docs.python.org/2/library/subprocess.html#frequently-used-arguments>
```

## 技术交流
```
Github: https://github.com/qiueer/cmds
QQ: 86877295
```
