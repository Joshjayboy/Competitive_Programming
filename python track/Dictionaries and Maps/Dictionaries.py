# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
contacts = {}
for _ in range(n):
    name, phone = input().split()
    contacts[name] = phone
    
while True:
    try:
        name = input()
        phone = contacts.get(name, "Not found")
        if phone == "Not found":
            print("Not found")
        else:
            print(f"{name}={phone}")
            
    except EOFError:
        break