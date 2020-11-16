#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import json
import os


sqlFo = open("test","r")

print ("文件名: ", sqlFo.name)
print ("是否已关闭 : ", sqlFo.closed)
print ("访问模式 : ", sqlFo.mode)

sqlStr = sqlFo.read(10)

print ("读取的字符串是 : ", sqlStr)

# 关闭打开的文件
sqlFo.close() 