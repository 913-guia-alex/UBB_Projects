class Node:
    def __init__(self, symbol, parent=None, left=None):
        #Initializes a Node in a tree.

        self.symbol = symbol
        self.parent = parent
        self.left = left

    def set_parent(self, parent):
        #Sets the parent node of the current node.

        self.parent = parent

    def set_left(self, left):
        #Sets the left child node of the current node.
        
        self.left = left
