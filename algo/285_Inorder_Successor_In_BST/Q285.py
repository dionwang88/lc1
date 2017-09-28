class Solution:
    def successor(self, root, p):
        if not root:
            return None
        if root.val <= p.val:
            return self.successor(root.right, p)
        else:
            left = self.successor(root.left, p)
            return left if left else root

    def predecessor(self, root, p):
        if not root:
            return None
        if root.val >= p.val:
            return self.predecessor(root.right, p)
        else:
            right = predecessor(root.left, p)
            return right if right else root

    def inOrderSuccessor(self, root, p):
        '''
        Input: node, root // node is the node whose Inorder successor is needed.
        output: succ // succ is Inorder successor of node.

        1) If right subtree of node is not NULL, then succ lies in right subtree. Do following.
        Go to right subtree and return the node with minimum key value in right subtree.
        2) If right sbtree of node is NULL, then start from root and us search like technique. Do following.
        Travel down the tree, if a node’s data is greater than root’s data then go right side, otherwise go to left side.
        '''
        if not root:
            return None
        if p.right:
            node = p.right
            while node:
                node = node.left
            return node.val
        else:
            node = None
            while root:
                if p.val < root.val:
                    node = root
                    root = root.left
                elif p.val > root.val:
                    root = root.right
                else:
                    break
            return node

    def inorderSuccessor1(self, root, p):
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ
