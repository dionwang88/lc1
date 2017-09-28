class Solution:
    def getNumberOfConnectedGraph(self, n, edges):
        '''
        DFS with Recursion
        '''
        visited = [0] * n
        dic = {x : [] for x in xrange(n)}

        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])

        result = 0
        for i in xrange(n):
            if not visited[i]:
                self.dfs(i, dic, visited)
                result += 1
        return result

    def dfs(self, i, dic, visited):
        if visited[i]:
            return
        visited[i] = 1
        for j in dic[i]:
            self.dfs(j, dic, visited)

    def getNumberOfConnectedGraph1(self, n, edges):
        '''
        DFS with Iteration
        '''
        visited = [0] * n
        dic = {x : [] for x in xrange(n)}

        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])

        result = 0
        for i in xrange(n):
            if not visited[i]:
                result += 1
                stack = [i]
                while stack:
                    node = stack.pop()
                    if not visited[node]:
                        visited[node] = 1
                        for j in dic[node]:
                            stack.append(j)
        return result

    def getNumberOfConnectedGraph2(self, n, edges):
        '''
        BFS with Iteration
        '''
        from Queue import Queue
        visited = [0] * n
        dic = {x : [] for x in xrange(n)}

        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])

        result = 0
        for i in xrange(n):
            if not visited[i]:
                result += 1
                queue = Queue()
                queue.put(i)
                while not queue.empty():
                    node = queue.get()
                    if not visited[node]:
                        visited[node] = 1
                        for j in dic[node]:
                            queue.put(j)
        return result

sol = Solution()
print sol.getNumberOfConnectedGraph2(5, [[0, 1], [1, 2], [3, 4]])
