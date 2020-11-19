#!/usr/bin/python
# -*- coding: UTF-8 -*- 


# 生成二叉树
class TreeNode(object):
    '二叉树节点类'
    def __init__(self, data=None):
        self.type = data['type'] 
        self.name = data['name']
        self.value = data['value']
        self.first_line = data['first_line']
        self.first_column = data['first_column']
        self.last_line = data['last_line']
        self.last_column = data['last_column']
        self.left = data['left']
        self.right = data['right']


class jsonToTree(object):
    '二叉树类'
    # 初始化
    def __init__(self):
        self.node = None
        self.left = None
        self.right = None
        
    # 添加节点
    def create(self, data):
        self.node = TreeNode(data)
        root = node
        # 如果树是空的，则对根节点赋值
        if node.left <> '':
             
            self.root = node 
        else:
            currentNode = self.queue[0]
            if currentNode.left == None:
                currentNode.left = node 
            else: 
                currentNode.right = node 
    # 前序遍历
    def preOrderTraversal(self, root):
        # 遍历终止条件
        if root == None:
            return
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)


