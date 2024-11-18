class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority
    