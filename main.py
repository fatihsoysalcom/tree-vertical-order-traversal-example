import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_order_traversal(root):
    """
    Performs a vertical order traversal of a binary tree.
    Nodes are grouped by their horizontal distance from the root.
    Within each horizontal column, nodes are sorted by their level (depth).
    """
    if not root:
        return []

    # Dictionary to store nodes by their horizontal distance (HD).
    # Each HD maps to a list of (level, node_value) tuples.
    column_nodes = collections.defaultdict(list)

    # Queue for BFS: stores (node, horizontal_distance, level)
    queue = collections.deque([(root, 0, 0)])

    min_hd = 0
    max_hd = 0

    while queue:
        node, hd, level = queue.popleft()

        # Store the node's value along with its level
        column_nodes[hd].append((level, node.val))

        # Update min/max horizontal distances encountered
        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        # Enqueue left child: HD decreases by 1, level increases by 1
        if node.left:
            queue.append((node.left, hd - 1, level + 1))

        # Enqueue right child: HD increases by 1, level increases by 1
        if node.right:
            queue.append((node.right, hd + 1, level + 1))

    # Prepare the final result list
    result = []
    # Iterate from the minimum HD to the maximum HD to get columns in order
    for hd in range(min_hd, max_hd + 1):
        # Get all nodes for the current horizontal distance
        nodes_in_column = column_nodes[hd]
        # Sort nodes within the column primarily by level, then by value if levels are same
        nodes_in_column.sort(key=lambda x: (x[0], x[1])) # x[0] is level, x[1] is value
        # Extract just the values for the current column
        result.append([node_val for level, node_val in nodes_in_column])

    return result

# --- Example Usage ---
# Construct a sample tree:
#       3
#      / \
#     9  20
#       /  \
#      15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Tree structure:")
print("      3")
print("     / \")
print("    9  20")
print("      /  \")
print("     15   7")
print("\nPerforming Vertical Order Traversal...")

# Perform the traversal
output = vertical_order_traversal(root)

# Print the result
print("Vertical Order Traversal Output:")
for col_idx, column in enumerate(output):
    print(f"Column {col_idx + 1}: {column}")

# Another example tree:
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7
#      / \
#     8   9

print("\n--- Another Example ---")
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(7)
root2.left.right.left = TreeNode(8)
root2.left.right.right = TreeNode(9)

print("Tree structure:")
print("      1")
print("     / \")
print("    2   3")
print("   / \ / \")
print("  4  5 6  7")
print("     / \")
print("    8   9")
print("\nPerforming Vertical Order Traversal...")
output2 = vertical_order_traversal(root2)
print("Vertical Order Traversal Output:")
for col_idx, column in enumerate(output2):
    print(f"Column {col_idx + 1}: {column}")
