for i in range(int(input())):
    str_len = int(input())

    string = input()

    zc = oc = pz = 0
    for _ in range(str_len):
        if string[_] == "1":
            zc += 1
        else:
            oc += 1
        if i < str_len -1 and string[i] != string[i + 1]:
            pz += 1
            break
    if zc > oc or pz:
        print("No")
    else:
        print("Yes")