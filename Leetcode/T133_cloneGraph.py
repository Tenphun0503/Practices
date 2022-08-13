"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Example:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.cpdic = {}

    def cloneGraph(self, node: 'Node'):
        return self.copyNode(node)

    def copyNode(self, node: Node):
        if node is None:
            return None

        if node in self.cpdic:
            return self.cpdic[node]

        new = Node(node.val)
        self.cpdic[node] = new

        for i in node.neighbors:
            new.neighbors.append(self.copyNode(i))

        return new

