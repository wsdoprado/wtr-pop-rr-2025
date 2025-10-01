from scrapli.driver.core import EOSDriver

device = EOSDriver(host="2001:db8:100::101", auth_username="admin", auth_password="admin", auth_strict_key=False)
device.open()

output = device.send_command("show ip int brief")
print(output.result)

device.close()
