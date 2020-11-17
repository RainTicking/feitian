#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import json
import os


# 打开文件
sqlFo = open("abc.sql","r")
# 读取文件
sqlStr = sqlFo.read()
# 关闭打开的文件
sqlFo.close() 
# 生成Json
sqlJson = json.loads(sqlStr)


# 生成二叉树
class Node(object):
    '生成二叉树节点'
    def __init__(self, val=-1, left= None, right = None):
        self.val = val 
        self.left = left
        self.right = right

class Tree(object):
    '生成二叉树'
    # 初始化
    def __init__(self):
        self.root = Node()
        self.Queue = []
    # 添加节点
    def add(self, val):
        node = Node(val)
        if self.root.val == -1:
            self.root = node 
            self.Queue.append(self.root)
        else:
            currentNode = self.Queue[0]
            if currentNode.left == None:
                currentNode.left = node 
                self.Queue.append(node)
            else 
                currentNode.right = node 
                self.Queue.append(node)
                self.Queue.pop(0)




