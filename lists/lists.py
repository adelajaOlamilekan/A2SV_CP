if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        cmd = input().split()
        
        if cmd[0] == "print":
            print(arr)
        elif cmd[0] == "sort":
            arr.sort()
        elif cmd[0] == "pop":
            arr.pop()
        elif cmd[0] == "reverse":
            arr.reverse()
        elif cmd[0] == "insert":
            index = int(cmd[1])
            value = int(cmd[2])
            arr.insert(index, value)
        elif cmd[0] == "remove":
            value = int(cmd[1])
            arr.remove(value)
        elif cmd[0] == "append":
            value = int(cmd[1])
            arr.append(value)         