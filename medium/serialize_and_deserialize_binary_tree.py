from collections import deque

class Node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def serialize(self, root):
        self.s = ""
        def serial_traverse(root):
            if not root:
                return
            self.s += str(root.val)
            self.s += " "
            serial_traverse(root.left)
            serial_traverse(root.right)
        serial_traverse(root)
        return self.s
    def deserialize(self, data):
        data = data.split(" ")
        data = data[:len(data)-1]
        vals = deque(int(val) for val in data)
        def build_tree(min_val, max_val):
            if vals and min_val <= vals[0] <= max_val:
                node_val = vals.popleft()
                cur_node = Node(node_val)
                cur_node.left = build_tree(min_val, node_val)
                cur_node.right = build_tree(node_val, max_val)
                return cur_node
        root = build_tree(float('-infinity'), float('infinity') )
        return root
