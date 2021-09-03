"""
PYTHON加密解密字符串 - 谢耳朵的派森笔记
https://www.cnblogs.com/shld/p/10027710.html

安装依赖包：
pip install pycryptodome

python3字符串base64编解码
https://www.cnblogs.com/kanneiren/p/9981084.html

Base64解码 Base64编码 UTF8 GB2312 UTF16 GBK 二进制 十六进制 解密 - The X 在线工具
https://the-x.cn/base64

Python解码base64遇到Incorrect padding错误
https://www.cnblogs.com/wswang/p/7717997.html

python 字节型转字符串
https://blog.csdn.net/iwilldoitx/article/details/78041593
"""

import base64

from Crypto.Cipher import AES
from binascii import b2a_base64, a2b_base64


# rpad
def rpad(text, divisor: int, suffix):
    remain = len(text) % divisor
    if remain > 0:
        text += suffix * (divisor - remain)
    return text


# 加密加盐 编码
def encrypt(text, salt, key):
    fmtkey, fmtiv = map(lambda s: s.encode()[:16].ljust(16, b'\0'), (key, salt))
    cryptor = AES.new(fmtkey, AES.MODE_CBC, fmtiv)
    fmttext = rpad(text.encode(), 16, b'\0')
    ciphertext = cryptor.encrypt(fmttext)
    return str(b2a_base64(ciphertext))[2:-3].rstrip('=')


# 加密加盐 解码
def decrypt(text, salt, key):
    fmtkey, fmtiv = map(lambda s: s.encode()[:16].ljust(16, b'\0'), (key, salt))
    cryptor = AES.new(fmtkey, AES.MODE_CBC, fmtiv)
    fmttext = rpad(text, 4, '=')
    return cryptor.decrypt(a2b_base64(fmttext)).rstrip(b'\0').decode()


# 首先，Base64生成的编码都是ascii字符。
# 其次，python3中字符都为unicode编码，而b64encode函数的参数为byte类型，所以必须先转码。
# base64编码
def base64Encrypt(text):
    return base64.b64encode(text.encode("utf-8"))  # 将字符为unicode编码转换为utf-8编码


# base64解码
def base64Decrypt(text):
    return str(base64.b64decode(text), "utf-8")


# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
# base64编码 urlsafe
def base64_urlsafe_Encrypt(text):
    return base64.urlsafe_b64encode(text.encode("utf-8"))  # 将字符为unicode编码转换为utf-8编码


# base64解码 urlsafe
def base64_urlsafe_Decrypt(text):
    return str(base64.urlsafe_b64decode(text), "utf-8")


# test
def test_me():
    # key,salt应为16字节(汉字3字节，字母1字节)，不足的自动补空格，超过的取前16字节
    ciphertext = encrypt("我们的祖国是花园~", "JustYouKnow", "LC")
    plaintext = decrypt(ciphertext, "JustYouKnow", "LC")
    print(ciphertext)
    print(plaintext)

    ciphertext2 = base64Encrypt("JustYouKnow" + "~LC")
    plaintext2 = base64Decrypt("")
    print(ciphertext2)
    print(plaintext2)


# 将不可见的变成可见的 你知道的
def just_you_know():
    try:
        print('====== 开始：just_you_know')
        print('')
        # 开始正式操作
        with open('JustYouNeverKnow.txt', 'r', encoding='UTF-8') as f:
            thisData_plus_base64_str = f.read()
            # utf8 字符串 转 byte
            # str to bytes
            thisData_plus_base64_byte = bytes(thisData_plus_base64_str, encoding="utf8")
            # 将 thisData_plus_base64_byte 进行base64解码
            thisData_plus = base64Decrypt(thisData_plus_base64_byte)
            # 将thisData_plus进行加密加盐解码
            thisData = decrypt(thisData_plus, "JustYouKnow", "LC")
            print(thisData)
    except ValueError as e:
        print('====== ValueError:', e)
    except ZeroDivisionError as e:
        print('====== ZeroDivision:', e)
    except Exception as e:
        print('====== Exception:', e)
    else:
        print('====== 没有出错！')
    finally:
        print('====== 最后要执行的代码')


# 将可见的变成不可见的 你不知道的
def just_you_never_know():
    try:
        print('====== 开始：just_you_never_know======')
        print('')
        # 开始正式操作
        with open('JustYouKnow.txt', 'r', encoding='UTF-8') as f:
            thisData = f.read()
            # 将thisData进行加密加盐编码
            thisData_plus = encrypt(thisData, "JustYouKnow", "LC")
            # print(thisData_plus)
            # 将thisData_plus进行base64编码
            thisData_plus_base64_byte = base64Encrypt(thisData_plus)
            # byte 转 utf8 字符串
            # bytes to str
            thisData_plus_base64_str = str(thisData_plus_base64_byte, encoding="utf-8")
            print(thisData_plus_base64_str)
    except ValueError as e:
        print('====== ValueError:', e)
    except ZeroDivisionError as e:
        print('====== ZeroDivision:', e)
    except Exception as e:
        print('====== Exception:', e)
    else:
        print('====== 没有出错！')
    finally:
        print('====== 最后要执行的代码')


if __name__ == "__main__":
    # 测试一下
    # test_me()
    # 方法一
    # 执行 just_you_know() 之后 可见文本中
    # 你可获取 JustYouKnow/JustYouKnow.txt.zip 压缩包密码 即可进行解压
    # 你再次编辑之后
    # 将 JustYouKnow.txt 放 JustYouKnow目录下 得到文件路径如下 【JustYouKnow/JustYouKnow.txt】
    # 然后 执行我 将可见文件再次加密 解开注释即可执行
    # just_you_never_know()
    # 方法二
    # 上边说了很多废话 你直接新建一个文本文档 命名 JustYouKnow.txt 然后执行 just_you_never_know() 进行加密 更香啊
    # -------------------------------------------------
    # 执行我 将不可见加密文件 可见
    just_you_know()

