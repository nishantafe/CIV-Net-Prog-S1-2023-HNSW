players_1 = ["John", "David", "Max"]
players_2 = ["Sara", "Rita", "Sofia"]

for player_1 in players_1:
    for player_2 in players_2:
        print(player_1, "VS", player_2)

# 10.10.10.0:80
# 0.0.0.0:
# 255.255.255.255
#
# 192.168.0.1:80
# 192.168.0.2:80
# 192.168.0.3:80
# 192.168.0.4:80
# 192.168.0.1:443
# 192.168.0.2:443
# 192.168.0.3:443
# 192.168.0.4:443

ips = ["192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.4"]
ports = ["80", "443", "21"]

for ip in ips:
    for port in ports:
        # scan(ip, port)
        print(ip + ":" + port)
