import socket
import os
import struct
from ctypes import *

# IP packet Fields Description and packet decoding of sniffer raw packet
class IP(Structure):
	_fields_ = [("ihl",c_ubyte, 4),("version",c_ubyte, 4),("tos",c_ubyte),("len",c_ushort),("id",c_ushort),
("offset",c_ushort),("ttl",c_ubyte),("protocol_num",c_ubyte),("sum",c_ushort),("src",c_ulong),("dst",c_ulong) ]

	def __new__(self, socket_buffer=None):
		return self.from_buffer_copy(socket_buffer)

	def __init__(self, socket_buffer=None):
		# protocol name maping to protocol number  
		self.protocol_map = {1:"ICMP", 6:"TCP", 17:"UDP"}

		# Readable ip address
		self.src_address = socket.inet_ntoa(struct.pack("<L",self.src))
		self.dst_address = socket.inet_ntoa(struct.pack("<L",self.dst))
		
		# Readable protocol 
		try:
			self.protocol = self.protocol_map[self.protocol_num]
		except:
			self.protocol = str(self.protocol_num)







# Host Name Which is work as sniffer 
host = "127.0.0.1"

#check which os is use for sniffing if windows (nt) then perfome some special task 
if os.name == "nt":

	socket_protocol = socket.IPPROTO_IP
else:
	socket_protocol = socket.IPPROTO_ICMP
print '-----------------------------------------------------------------------------\n'
print 'Welcome to IP Packet Sniffer Tools'
print 'If any ip packet arrive or leave you system then this tool is able to capture them\n'
print '-------------------------------------------------------------------------------\n'

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind((host, 0))

sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

if os.name == "nt":
	sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

print 'Now Tell Me what you want to DO\n'
print '1. Print Raw IP RAW Packet as Encoded\n'
print '2. Print Decoded IP Packet\n'
option=raw_input()

try:
	while True:
		# Sniffing Packet Reading 
		
		if (option == '1'):
			raw_buffer = sniffer.recvfrom(65565)
			print raw_buffer
			print '\n'
		if (option == '2'):
			raw_buffer = sniffer.recvfrom(65565)[0]
			# IP Header extract from packet that is starting 160 bit or 20 bytes. 
			ip_header = IP(raw_buffer[0:20])
			# print protocol and source packet address or destinaiton packet address
			print "%s %s ----> %s" % (ip_header.protocol, ip_header.src_address, ip_header.dst_address)
		# handle CTRL-C
except KeyboardInterrupt:
	# if we're using Windows, turn off promiscuous mode
	if os.name == "nt":
		sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


