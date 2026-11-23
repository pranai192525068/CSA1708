def minimax(depth, node, is_max):
    if depth == 2:
        return node

    if is_max:
        return max(minimax(depth+1, x, False) for x in node)
    else:
        return min(minimax(depth+1, x, True) for x in node)

tree = [[3, 5], [2, 9]]

print("Best Value:", minimax(0, tree, True))
