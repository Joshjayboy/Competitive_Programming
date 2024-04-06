def longest_good_segment(n, s):
    max_length = 1
    current_length = 1

    for i in range(2, n):
        if s[i] > s[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    max_length = max(max_length, current_length)
    return max_length