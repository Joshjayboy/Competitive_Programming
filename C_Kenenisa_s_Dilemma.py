def sort_with_swaps(n, a):
    swaps = []
    # Create a list of indices from 0 to n-1
    indices = list(range(n))
    
    # Sort indices based on values in the array
    indices.sort(key=lambda x: a[x])
    
    # Create a list to track current positions
    pos = list(range(n))
    
    for i in range(n):
        correct_index = indices[i]
        if pos[i] != correct_index:
            # Find where the correct_index is currently located
            swap_index = pos.index(correct_index)
            
            # Perform the swap
            a[i], a[swap_index] = a[swap_index], a[i]
            pos[i], pos[swap_index] = pos[swap_index], pos[i]
            swaps.append((i, swap_index))
    
    return swaps

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:]))
    
    swaps = sort_with_swaps(n, a)
    
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

if __name__ == "__main__":
    main()
