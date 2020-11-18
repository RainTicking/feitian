#!/usr/bin/python
# -*- coding: UTF-8 -*- 


# 生成二叉树
class TreeNode(object):
    '二叉树节点类'
    def __init__(self, val=None, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

class BinTree(object):
    '二叉树类'
    # 初始化
    def __init__(self):
        self.root = None
        self.queue = []
    # 添加节点
    def add(self, val):
        node = TreeNode(val)
        # 如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node 
            self.queue.append(self.root)
        else:
            currentNode = self.queue[0]
            if currentNode.left == None:
                currentNode.left = node 
                self.queue.append(currentNode.left)
            else: 
                currentNode.right = node 
                self.queue.append(currentNode.right)
                self.queue.pop(0)
    # 前序遍历
    def preOrderTraversal(self, root):
        # 遍历终止条件
        if root == None:
            return
        print(root.val)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)


