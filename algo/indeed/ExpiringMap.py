'''
可以使用PriorityQueue
'''
class ExpiringMap:
    from time import time
    def __init__(self):
        self.emap = {}
        self.threshold = 3

    def put(self, node):
        emap[node.key] = node.expiretime

    def get(self, key):
        if key in emap:
            now = time()
            if now - emap[key] < self.threshold:
                return emap[key]
            else:
                del emap[key]

class Node:
    def __init__(self, key, expiretime):
        self.key = key
        self.expiretime = expiretime
