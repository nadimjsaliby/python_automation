import os
import socket
import subprocess
import netifaces

from scapy.all import *

def get_ip_address(iface):
    # Get the IP address of the specified interface
    iface_data = netifaces.ifaddresses(iface)
    return iface_data[netifaces.AF_INET][0]['addr']

def scan_network(subnet):
    # Scan the specified subnet for hosts
    hosts = []
    for host in range(1, 256):
        address = subnet + str(host)
        response = os.system("ping -c 1 " + address)
        if response == 0:
            hosts.append(address)
    return hosts

def get_domain_name(ip_address):
    # Get the domain name associated with an IP address
    try:
        domain = socket.gethostbyaddr(ip_address)[0]
    except:
        domain = "Unresolved"
    return domain

def monitor_network(subnet):
    # Monitor network activity and identify devices and services
    hosts = scan_network(subnet)
    for host in hosts:
        print("[+] Host found:", host)
        domain = get_domain_name(host)
        print("[+] Domain name:", domain)

def perform_security_scan(subnet):
    # Perform a security scan of the specified subnet
    print("[+] Performing security scan...")
    subprocess.call(["nmap", "-sS", "-sV", "-p-", subnet])

def extract_websites(packet):
    # Extract the websites being accessed by clients
    if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
        domain = packet.getlayer(DNS).qd.qname.decode()
        print("[+] Client is accessing:", domain)

def sniff_network(subnet):
    # Sniff network packets and extract websites being accessed
    sniff(prn=extract_websites, filter="udp and port 53")

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(scapy.DNSRR):
        print("[+] DNS Request: " + packet[scapy.DNSQR].qname.decode("utf-8"))

if __name__ == '__main__':
    # Get the interface to be used for network analysis
    iface = input("Enter the network interface to be used: ")
    ip_address = get_ip_address(iface)
    subnet = ip_address + "/24"
    print("[+] Using subnet:", subnet)
    print("[+] Monitoring network activity...")
    monitor_network(subnet)
    print("[+] Extracting websites being accessed...")
    sniff_network(subnet)
    perform_security_scan(subnet)
    interface = input("Enter the network interface to monitor: ")
    sniff(interface)
