import collections
class Node:
    def __init__(self, data) :
        self.left = None
        self.right= None
        self.data = data
    def insert (self, data):
        if self.data is None:
            self.data = data 
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
                        
def inOrderPrint(r):
    if r is None:
        return
    else:
        inOrderPrint(r.left)
        print(r.data, end=' ')
        inOrderPrint(r.right)
    
        
def preOrderPrint(r):
    if r is None:
        return 
    else:
        print(r.data, end=' ')
        preOrderPrint(r.left)
        preOrderPrint(r.right)
        
def postOrderPrint(r):
    if r is None:
        return
    else:
        print(r.data, end=" ")
        postOrderPrint(r.right)
        postOrderPrint(r.left)

def makeList(r):
    if r is None:
        return 
    else:
        d[r.data] = []
        makeList(r.left)
        if r.left:
            d[r.data]
            d[r.data].append(r.left.data)
        makeList(r.right)
        if r.right:
            d[r.data].append(r.right.data)
            
        return d

visited = []
queue = []

def bfs(visited, aList, node):
    
    
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print (m, end=" ")
        for x in aList[m]:
            if x not in visited:
            
                visited.append(x)
                queue.append(x)


def bfs_collection(als):
    queue = collections
    
    
if __name__ == '__main__':
    root = Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')
    
    
    d ={}
    aList = makeList(root)
    
    bfs(visited, aList, 'g')
    
    
    