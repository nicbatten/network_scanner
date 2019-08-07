#!/usr/bin/env python

import scapy.all as scapy
#importing scapy and initialising as a variable

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
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    #srp allows us to send packets with custom ether part/layer

    #print(answered_list.summary())
    #this gives us a summary of all the data returned

#loop through all elements in the answered_list
    for element in answered_list:
        #print(element[1].show())
        #show everything in the packet

        #show only IP address of source and MAC
        print(element[1].psrc)
        print(element[1].hwsrc)
        print("-------------------------------------------------------------------------")

scan("10.0.2.1/24")

