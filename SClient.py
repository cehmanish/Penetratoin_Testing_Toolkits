import threading
import paramiko
import subprocess
import sys
import getopt 
import time

global ip
global user
global passwd

def ssh_command(ip, user, passwd):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=user, password=passwd)
	shell = client.invoke_shell()
	print 'Type the Command and press Enter for Response '

	while True:
		print shell.recv(9999)
		time.sleep(1)
		command=raw_input()
		shell.send(command + '\n')
		print shell.recv(9999)
		



def usage():
	print "Sclient is a SSH Light Weight Client\n"
	print "./Sclient [options]\n"
	print "Option -\n"
	print "-h / --help - For Help \n"
	print "-t / --target - For SSH Server IP Address\n"
	print "-u / --user - For SSH USer Name\n"
	print "-p / --passwd - For SSH Password\n"



def main():
	
	if not len(sys.argv[1:]):
		usage()

	# read the commandline options

	try:
		opts, args = getopt.getopt(sys.argv[1:],"h:t:u:p:",["help","target","user","passwd"]) 
		for o,a in opts:
			if o in ("-h","--help"):
				usage()
			elif o in ("-t","--target"):
				ip = a
			elif o in ("-u", "--user"):
				user = a
			elif o in ("-p", "--passwd"):
				passwd = a
			else:
				assert False,"Unhandled Option"

		ssh_command(ip,user,passwd)
        except getopt.GetoptError as err:     
		print str(err)
	        usage()

	
main()




