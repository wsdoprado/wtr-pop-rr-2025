#Dicionário - dict
iface1 = {"name": "Ethernet 1", "description": "CUSTOMER A", "mtu": 1500, "Enabled": True, "ip4": "192.168.100.1/24", "ip6": None}
iface2 = {"name": "Ethernet 2", "description": "CUSTOMER B", "mtu": 1500, "Enabled": False, "ip4": None, "ip6": "2001:db8:100::1/64"}
iface3 = {"name": "lo0", "description": "loopback", "mtu": 1500, "Enabled": True, "ip4": "172.16.100.1", "ip6": "2001:db8:200::1/64"}

iface_list = [iface1, iface2, iface3]

#Dicionário - dict + Listas - list
switch1 = {"name": "switch1-pop-rr", "sn": "ABCDEF", "so": "iosxr", "fabricante": "cisco", "type": "ncs5501", "interfaces": iface_list}

print(f"name: {switch1["name"]} - interfaces: {switch1["interfaces"]}")

for iface in switch1["interfaces"]:
    print(iface["name"])
