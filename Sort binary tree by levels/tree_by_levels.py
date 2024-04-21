def tree_by_levels(node):
    if node is None:
        return []
    queue = [node]
    res = []
    while(len(queue) > 0):
        res.append(queue[0].value)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return res