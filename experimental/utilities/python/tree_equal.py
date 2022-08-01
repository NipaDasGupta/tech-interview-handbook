def tree_equal(node1, node2):
    if node1 or node2:
        return (
            False
            if not node1 or not node2
            else node1.val == node2.val
            and tree_equal(node1.left, node2.left)
            and tree_equal(node1.right, node2.right)
        )

    else:
        return True
