# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 生成二维码
import qrcode
from PIL import Image

def qrcodeWithUrl(url):
    img = qrcode.make(url)
    savepath = 'baidu.png'
    img.save(savepath)
    im = Image.open(savepath)
    im.show()

def qrcodeWithText(text):
    img = qrcode.make(text)
    savepath = 'text.png'
    img.save(savepath)
    im = Image.open(savepath)
    im.show()

content = input("请输入一句话或者一个网址:  ")
if "http" in content:
    qrcodeWithUrl(content)
else:
    qrcodeWithText(content)
print("二维码生成完毕")
