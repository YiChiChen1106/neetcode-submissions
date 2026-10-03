from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # 1. 所有字符都放进图里
        adj = {c: set() for word in words for c in word}

        # 2. 比较相邻单词，建立字母之间的关系
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            minLen = min(len(w1), len(w2))

            # 非法情况：
            # abc 在 ab 前面
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # 找第一个不同字符
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # 0 = 没访问
        # 1 = 正在访问
        # 2 = 已完成
        state = {}
        res = []

        def dfs(c):
            if c in state:
                # 正在当前路径中 -> 有环
                if state[c] == 1:
                    return False
                
                # 已经处理完
                if state[c] == 2:
                    return True

            state[c] = 1

            for nei in adj[c]:
                if not dfs(nei):
                    return False

            state[c] = 2

            # 后序加入
            res.append(c)

            return True

        # 3. 对所有字符 DFS
        for c in adj:
            if not dfs(c):
                return ""

        # DFS 后序得到的是反向拓扑序
        res.reverse()

        return "".join(res)