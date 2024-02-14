if __name__ == '__main__':
    N = int(input())
    records = []
    for _ in range(N):
        name = input()
        score = float(input())
        records.append((score, name))
        
    records.sort()
    lowest_score = records[0][0]
    
    # find the second lowest score
    for record in records:
        if record[0] != lowest_score:
            second_lowest_score = record[0]
            break
    
    for record in records:
        if record[0] == second_lowest_score:
            print(record[1])