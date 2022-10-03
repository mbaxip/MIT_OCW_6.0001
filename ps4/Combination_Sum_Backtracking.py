def comb_sum(candidates, target):
    res = []
    cur = []

    def dfs(i, total):
        if total == target:
            res.append(cur.copy())
            return

        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        dfs(i, total + candidates[i])

        cur.pop()
        dfs(i+1, total)

    dfs(0,0)
    return res

candidates = [2,3,5]
target = 8
print(comb_sum(candidates, target))