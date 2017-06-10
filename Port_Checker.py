import threading
import paramiko
import subprocess
import sys
import getopt 
import time
import socket


print '---------------------------------------------------------------------------------\n'
print 'Welcome to Interective Easy to Use Port Scanner Utility\n'

print 'We are Happy to help you \n '

print 'Frist Enter the Ip Address of Remote Machine  '

ip=raw_input()

soc= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print 'Now Tell Me What You Want to Do With Remote Machine\n'

print '1. Single Port Scanning\n'
print '2. Multiple Port Scanning by Port Range\n'
print '3. Default Port Scanning \n'

option =raw_input()

if option == '1':
	print "Enter the Port no Which You Want to Examine \t"
	port=input()
	try: 
		soc.connect((ip,port))
		print 'Port %s is Open' %(port)
	except:
		print 'Port %s is Close' %(port)

if option == '2':
	print 'Enter The Range of Port  \n'
	print 'Enter Starting Port No.'
	start_port=input()
	print 'Enter End Port No. '
	end_port=input()
	
	for port in range(start_port,end_port+1):
		try:		
			soc.connect((ip,port))
			print 'Port %s is Open' %(port)
		except:		
			print 'Port %s is Close ' %(port)


if option == '3':
	default_port=[21,22,23,25,80,139,443,445,8080]
	
	for port in default_port:
		try:	
			soc.connect((ip,port))
			print 'Port %s is Open' %(port)
		except:	
			print 'Port %s is Close ' %(port)









