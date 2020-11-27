

class Node: # node object
    def __init__(self, key): 
        self.data = key  
        self.left = None
        self.right = None

    def get_children(self):
        return str(self.left.data) + " | " + str(self.right.data)


levelOrder = []
# Function to  print level order traversal of tree 
def printLevelOrder(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i)
  

# Print nodes at a given level 
def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print("%d" %(root.data))
        levelOrder.append(root.data)
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1) 


# calculates the height of each subtree
def height(node): 
    if node is None: 
        return 0 
    else:
        lheight = height(node.left) 
        rheight = height(node.right) 

        # selects the larger one
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1
  
# Driver program to test above function 
root = Node(4) 
root.left = Node(1) 
root.right = Node(7) 
root.left.left = Node(3) 
root.left.right = Node(5) 
root.left.right.right = Node(2) 
root.left.right.left = Node(6) 
root.left.right.right.left = Node(8) 
root.left.right.left.right = Node(9)
  
print("Level order traversal of binary tree is -")
printLevelOrder(root)
print(levelOrder)

# The Breadth-First Traversal visits every node and edge so...
# The number of operations is therefor n + e
# n -> number of verticies, e -> number of edges
# So this means O(n) (Big-O-Notation)

# However in a graph with maximum edges, the adjecency matrix is full
# So n edges and n^2 edges, therefor giving... giving vn^2 + n
# The Time Complexity: O(n^2)
# This is the max amount of searches to be made.