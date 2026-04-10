# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.ser = ""
        self.ser_dfs(root)
        return self.ser
    def ser_dfs(self, root: Optional[TreeNode]):
        if root is None:
            self.ser = self.ser + "N" + ","
            return
        else:
            self.ser = self.ser + str(root.val) + ","
        self.ser_dfs(root.left)
        self.ser_dfs(root.right)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.str_tree = data.split(",")[:-1]
        self.i = 0
        return self.des_dfs()

    def des_dfs(self) -> Optional[TreeNode]:
        if self.str_tree[self.i] == "N":
            self.i += 1
            return None
        node = TreeNode(int(self.str_tree[self.i]))
        self.i += 1
        node.left = self.des_dfs()
        node.right = self.des_dfs()
        return node

