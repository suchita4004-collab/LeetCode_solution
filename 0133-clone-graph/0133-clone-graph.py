class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None

        cloned = {}

        def dfs(current):
            if current in cloned:
                return cloned[current]

            copy = Node(current.val)
            cloned[current] = copy

            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)