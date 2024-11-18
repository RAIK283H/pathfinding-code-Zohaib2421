# Pathfinding Starter Code


Customer Requirements:
The Random player should generate a random path from the start node to the exit node and visit the target node at some point in the traversal

    This requirement is met by doing a random graph DFS traversal.
    Starting at the start node, the first objective is reach the target node. This ensures that half of the customer requirements will be met.
    Because of this, the first part of path is simply a get_path function from start to target.
    Once we've gotten that path, then the second half of the requirement is to exit at the target node.
    Because of this, the second part of path is the value of get_path from target to end.
    In the code, you'll notice that there is a path.pop in between the get_path from start to target and get_path from target to end. This is because the get_path function is
    inclusive for its start and end parameters, so the path.pop makes sure that player doesn't just sit at the target node during the traversal.

    Explaining the get_path algorithm, it is essentially a DFS traversal while adding neighbours to the stack randomly, hence why get_neighbours does a shuffle on the current nodes' neighbours.
    The node has an equal chance to visit any neighbour of the current node. 
    There is not a visited set keeping track of which nodes the player has already visited. For this reason, this algorithm may not be great for very large graphs,
    however, it ensures that there will always be a path as per the customer requirements and the path will always be random.

    For the extra statistic, I have chosen to show the amount of unique nodes visited. This gives insight into how much of the actual graph is explored. This is useful because if there are 30 nodes in a graph and the random path is bouncing between two nodes and then goes to the end node, it may be hard to see that by simply looking at the random path because of its long length.
    This statistic will make it easier to understand cases like that and others similar.

On homework 6, I attempted extra credit with the "implement the heapq" bullet point