# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    m = int(input().strip())
    
    print(str(pow(a, b)))
    print(str(pow(a, b, m)))
