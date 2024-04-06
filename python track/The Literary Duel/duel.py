def predict_game_outcome(n, powers):
    # Initialize pointers for left and right ends of the remaining books
    left = 0
    right = n - 1

    # Initialize cumulative sums of magical powers for Hermione and Harry
    hermione_score = 0
    harry_score = 0

    # Iterate until there are no more books left
    while left <= right:
        # Hermione's turn
        if powers[left] > powers[right]:
            hermione_score += powers[left]
            left += 1
        else:
            hermione_score += powers[right]
            right -= 1

        # Harry's turn
        if left <= right:
            if powers[left] > powers[right]:
                harry_score += powers[left]
                left += 1
            else:
                harry_score += powers[right]
                right -= 1

    return hermione_score, harry_score

# Input reading
n = int(input())
powers = list(map(int, input().split()))

# Predict the outcome
hermione_score, harry_score = predict_game_outcome(n, powers)

# Output the result
print(hermione_score, harry_score)
