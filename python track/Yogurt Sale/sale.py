# Function to calculate the minimum cost of buying n yogurts
def min_cost(t, cases):
    for case in cases:
        n, a, b = case
        cost_individually = n * a  # Cost of buying all yogurts individually
        cost_promotion = (n // 2) * b + (n % 2) * a  # Cost of buying yogurts using promotion
        print(min(cost_individually, cost_promotion))

# Input handling
t = int(input())  # Number of test cases
cases = []
for _ in range(t):
    n, a, b = map(int, input().split())
    cases.append((n, a, b))

# Calculate and output the minimum cost for each test case
min_cost(t, cases)
