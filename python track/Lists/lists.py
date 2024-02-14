if __name__ == '__main__':
    N = int(input())
    my_list = []
    for i in range(N):
        line = input().split()
        command = line[0]
        if command == 'insert':
            my_list.insert(int(line[1]), int(line[2]))
        elif command == 'print':
            print(my_list)
        elif command == 'remove':
            my_list.remove(int(line[1]))
        elif command == 'append':
            my_list.append(int(line[1]))
        elif command == 'sort':
            my_list.sort()
        elif command == 'pop':
            my_list.pop()
        elif command == 'reverse':
            my_list.reverse()
