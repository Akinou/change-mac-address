import subprocess
import random

# Generate a random MAC address
def random_mac():
    return ':'.join([random.choice('0123456789ABCDEF') + random.choice('0123456789ABCDEF') for i in range(6)])

# Change the MAC address of the device
def change_mac(interface, mac):
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])
    subprocess.call(['ifconfig', interface, 'up'])

# Usage example
interface = 'eth0'
new_mac = random_mac()
print(f"Changing MAC address of {interface} to {new_mac}")
change_mac(interface, new_mac)
