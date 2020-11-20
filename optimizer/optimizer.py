#!/usr/bin/python
# -*- coding: UTF-8 -*- 


class TreeNode(object):
    '二叉树节点类'
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class JsonToTree(object):
    '二叉树类'
    # 初始化
    def __init__(self, data = None):
        node = TreeNode(data.copy())
        self.root = node
        self.queue = []
        self.queue.append(node)
    # 生成树
    def createTree(self):
        if self.root.data is None:
            return
        while self.queue:
            tmpNode = self.queue[0]
            if tmpNode.data['left'] != '':
                node = TreeNode(tmpNode.data['left'])
                tmpNode.left = node
                self.queue.append(node)
                tmpNode.data['left'] = ''
            elif tmpNode.data['right'] != '':
                node = TreeNode(tmpNode.data['right'])
                tmpNode.right = node
                self.queue.append(node)
                tmpNode.data['right'] = ''
            else:
                self.queue.pop(0)
    # 前序遍历
    def preOrderTraversal(self, root):
        # 遍历终止条件
        if root == None:
            return
        print(root.data['name'])
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)


