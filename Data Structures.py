#Linked Lists 

class Node:
    def __init__(self, data):
        '''

        :param data:
        '''
        self.data = data
        self.next = None


class BinaryTree:
    def __init__(self, data, left, right):
        '''

        :param data:
        :param left:
        :param right:
        '''
        self.left = left
        self.right = right
        self.data = data
