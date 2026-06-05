from leetcode_py import GraphNode

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # Time: O(?)
    # Space: O(?)
    def clone_graph(self, node: GraphNode | None) -> GraphNode | None:
        
        oldToNew = {}

        '''
            If the input node is null, return null.
            Create a map to store original nodes -> cloned nodes.
            Start DFS from the given node:

                If the node is already in the map, return its clone.
                Create a new node with the same value.
                Store it in the map.
                Recursively clone all neighbors and add them to the clone’s neighbor list.

            Return the cloned node corresponding to the starting node.
        '''


        def dfs(node):
            if node.val in oldToNew:
                return oldToNew[node.val]
            
            # If the node is already in the map, return its clone.
            # Create a new node with the same value.
            # Store it in the map.
            # Recursively clone all neighbors and add them to the clone’s neighbor list.
            copy = GraphNode(node.val)

            oldToNew[node.val] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        # If the input node is null, return null.
        if not node:
            return
        return(dfs(node))
        