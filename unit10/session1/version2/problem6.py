"""
You are organizing the seating arrangement for a big awards ceremony and want to make a copy for your assistant. The seating arrangement is stored in a graph where each Node value val is the name of a celebrity guest at the ceremony and its array neighbors are all the guests sitting in seats adjacent to the celebrity.

Given a reference to a Node in the original seating arrangement seat, make a deep copy (clone) of the seating arrangement. Return the copy of the given node.

We have provided a function compare_graphs() to help with testing this function. To use this function, pass in the given node seat and the copy of that node your function copy_seating() returns. If the two graphs are clones of each other, the function will return True. Otherwise, the function will return False.
""""
class Node():
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
def copy_seating(seat: Node) -> Node:
    """
    Deep-clone an (undirected) seating-arrangement graph.

    Args
    ----
    seat : Node
        Any node in the original graph (may be part of a cycle).

    Returns
    -------
    Node
        The node that corresponds to *seat* in the cloned graph.
    """
    if seat is None:
        return None

    # hash-map: original node  ➜  cloned node
    clones = {}

    def dfs(node: Node) -> Node:
        """Return the clone of *node*, creating it (and its edges) on demand."""
        if node in clones:                     # already cloned
            return clones[node]

        # 1) create shallow clone (no neighbours yet)
        clone = Node(node.val)
        clones[node] = clone

        # 2) recursively clone neighbours
        for nbr in node.neighbors:
            clone.neighbors.append(dfs(nbr))

        return clone

    return dfs(seat)
