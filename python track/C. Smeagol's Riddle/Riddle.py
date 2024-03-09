def min_changes_to_palindrome(word):
    changes = 0
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            changes += 1
    return changes

# Read input
n = int(input())
words = [input().strip() for _ in range(n)]

# Process each word and output the result
for word in words:
    print(min_changes_to_palindrome(word))
