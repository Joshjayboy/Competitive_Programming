class UnionFind:
    def __init__(self):
        self.parent = {}
        
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

# Read inputs
n = int(input())
valya = input().strip()
tolya = input().strip()

# Initialize union-find for lowercase English letters
uf = UnionFind()

# Build equivalences for mismatching letters
for v, t in zip(valya, tolya):
    if v != t:
        uf.union(v, t)

# Collect spells by finding connected components
spells = []
visited = set()

for c in "abcdefghijklmnopqrstuvwxyz":
    root = uf.find(c)
    if root not in visited:
        # Find all letters in this component
        component = [ch for ch in "abcdefghijklmnopqrstuvwxyz" if uf.find(ch) == root]
        visited.add(root)
        
        # Add spells to connect each letter to the representative
        for i in range(1, len(component)):
            spells.append((component[0], component[i]))

# Output the result
print(len(spells))
for spell in spells:
    print(spell[0], spell[1])
