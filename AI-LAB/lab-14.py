def alphabeta(depth, node, alpha, beta, is_max):
    if depth == 2:
        return node

    if is_max:
        value = -999
        for child in node:
            value = max(value, alphabeta(depth+1, child, alpha, beta, False))
            alpha = max(alpha, value)

            if alpha >= beta:
                break
        return value

    else:
        value = 999
        for child in node:
            value = min(value, alphabeta(depth+1, child, alpha, beta, True))
            beta = min(beta, value)

            if beta <= alpha:
                break
        return value

tree = [[3, 5], [2, 9]]

print("Best Value:", alphabeta(0, tree, -999, 999, True))
