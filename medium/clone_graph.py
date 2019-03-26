"""
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph 
contains a val (int) and a list (List[Node]) of its neighbors.

Time: O(N)
Space: O(N)
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        queue = collections.deque()
        clones = {}
        clones[node] = Node(node.val, [])
        queue.append(node)
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                clones[curr].neighbors.append(clones[neighbor])
        return clones[node]