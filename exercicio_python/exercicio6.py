"""
Exercício 6 - Dicionários com Listas Aninhadas em Python
--------------------------------------------------------
Este exercício apresenta como criar e manipular dicionários que contém listas
de outros dicionários. Este é um padrão comum ao trabalhar com APIs ou dados
de automação de redes.

Objetivos:
1. Criar dicionários representando interfaces.
2. Criar um dicionário representando um switch com interfaces.
3. Acessar e iterar sobre dados aninhados.
"""

# Interfaces representadas como dicionários
iface1 = {
    "name": "Ethernet 1",
    "description": "CUSTOMER A",
    "mtu": 1500,
    "enabled": True,
    "ip4": "192.168.100.1/24",
    "ip6": None
}

iface2 = {
    "name": "Ethernet 2",
    "description": "CUSTOMER B",
    "mtu": 1500,
    "enabled": False,
    "ip4": None,
    "ip6": "2001:db8:100::1/64"
}

iface3 = {
    "name": "lo0",
    "description": "loopback",
    "mtu": 1500,
    "enabled": True,
    "ip4": "172.16.100.1",
    "ip6": "2001:db8:200::1/64"
}

# Lista de interfaces
iface_list = [iface1, iface2, iface3]

# Dicionário representando um switch
switch1 = {
    "name": "switch1-pop-rr",
    "sn": "ABCDEF",
    "so": "iosxr",
    "fabricante": "cisco",
    "type": "ncs5501",
    "interfaces": iface_list
}

# Mostrar informações do switch
print(f"name: {switch1['name']} - interfaces: {switch1['interfaces']}")

# Iterar sobre interfaces e mostrar seus nomes
print("\n--- Interfaces do Switch ---")
for iface in switch1["interfaces"]:
    print(f"Interface: {iface['name']}")
