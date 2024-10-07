# test_cases = int(input())
# for i in range(test_cases):
#     val = int(input())

MOD = 10**9 + 7

# Function to generate all palindromic numbers up to 40000
def generate_palindromes(limit):
    palindromes = []
    
    # Single digit palindromes
    for i in range(1, 10):
        palindromes.append(i)
    
    # Two-digit and more palindromes
    for i in range(1, 400):
        s = str(i)
        palindromes.append(int(s + s[::-1]))  # Even length palindromes
        palindromes.append(int(s + s[-2::-1]))  # Odd length palindromes
    
    return [p for p in palindromes if p <= limit]

# Main solution function
def solve():
    # Step 1: Generate all palindromic numbers up to 40000
    palindromes = generate_palindromes(40000)
    
    # Step 2: Initialize DP array
    max_n = 40000
    dp = [0] * (max_n + 1)
    dp[0] = 1  # Base case, 1 way to sum to 0 (using no numbers)
    
    # Step 3: Fill DP array using palindromes
    for p in palindromes:
        for i in range(p, max_n + 1):
            dp[i] = (dp[i] + dp[i - p]) % MOD
    
    # Step 4: Read input and process each test case
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(dp[n])

# Run the solution
solve()
