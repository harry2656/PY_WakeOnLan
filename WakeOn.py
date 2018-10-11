#! /usr/bin/env python
# coding=utf-8

import socket, sys
import struct

def create_magic_packet(mac):
    #创建魔术包
    spliter = ""
    if mac.count(":") == 5:
        spliter = ":"
    if mac.count("-") == 5:
        spliter = "-"

    if spliter == "":
        print("MAC address should be like XX:XX:XX:XX:XX:XX / XX-XX-XX-XX-XX-XX")
        sys.exit()

    parts = mac.split(spliter)
    strMac = ""
    for var in parts:
        strMac += var

    # print(strMac)

    data = b'FFFFFFFFFFFF' + (strMac * 16).encode()
    packet = b''
    length = len(data)
    for i in range(0, length, 2):
        s = int(data[i:i + 2], 16)
        # print(s)
        packet += struct.pack(b'B', s)
    return packet

def send_magic_packet(mac):
    #发送魔术包
    magic_packet=create_magic_packet(mac)
    dest = ('255.255.255.255', 9)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # print(packet)
    s.sendto(magic_packet, dest)
    print("WOL packet %d bytes sent !" % len(magic_packet))

def main():
    mac='B8-97-5A-7F-8C-A4'
    #mac='B8-97-5A-82-B8-0C'
    send_magic_packet(mac)



if __name__=='__main__':
    main()
