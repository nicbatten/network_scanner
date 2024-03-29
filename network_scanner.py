#!/usr/bin/env python

import optparse
import scapy.all as scapy
#importing scapy and initialising as a variable

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP or IP Range")
    (options, arguments) = parser.parse_args()
    if not options.target:
        #code to handle error
        parser.error("[-] Please specify a target IP or range of IPs. Use --help for more info.")
    return options

def scan(ip):
    #scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)

    #arp_request.show()
    #arp_request.pdst=ip
    #print(arp_request.summary())

    #scapy.ls(scapy.ARP())
    #this lists all the values you can set with scapy

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #broadcast.show()
    #scapy.ls(scapy.Ether())
    #print(broadcast.summary())

    arp_request_broadcast = broadcast/arp_request
    #creating our packet to send

    #print(arp_request_broadcast.summary())
    #arp_request_broadcast.show()

    #answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    #srp allows us to send packets with custom ether part/layer

    #print(answered_list.summary())
    #this gives us a summary of all the data returned

    clients_list = []

    #loop through all elements in the answered_list
    for element in answered_list:
        #print(element[1].show())
        #show everything in the packet

        client_dict={"ip":element[1].psrc , "mac": element[1].hwsrc}
        clients_list.append(client_dict)
        #show only IP address of source and MAC
        #print(element[1].psrc + "\t\t" + element[1].hwsrc)
    return clients_list

def print_result(results_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()

scan_result = scan(options.target)
print_result(scan_result)

