n, m = list(map(int, input().split(" ")))

server_map = {}

for _ in range(n):
    server, ip = input().split(" ")
    server_map[ip] = server

for _ in range(m):
    cmd, ip = input().split(" ")
    print(f"{cmd} {ip} #{server_map[ip[0:-1]]}")
