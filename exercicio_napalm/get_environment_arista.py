from napalm import get_network_driver

driver = get_network_driver("eos")
device = driver("2001:db8:100::101", "admin", "admin")
device.open()

print(device.get_environment())

device.close()
