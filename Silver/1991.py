import sys

n = int(sys.stdin.readline().strip())
adj = {}

for _ in range(n):
    parent, left, right = sys.stdin.readline().split()
    adj[parent] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(adj[root][0])
        preorder(adj[root][1])

def midorder(root):
    if root != '.':
        midorder(adj[root][0])
        print(root, end='')
        midorder(adj[root][1])

def lastorder(root):
    if root != '.':
        lastorder(adj[root][0])
        lastorder(adj[root][1])
        print(root, end='')


preorder('A')
print()
midorder('A')
print()
lastorder('A')