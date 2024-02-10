n, m = input().split(" ")

n = int(n)
m = int(m)

server_map = {}

for i in range(n):
    server, ip = input().split(" ")
    server_map[ip] = server

for i in range(m):
    cmd, ip = input().split(" ")
    ip = ip [0:len(ip)-1]
    srvr = server_map[ip]
    print(f"{cmd} {ip}; #{server_map[ip]}")
