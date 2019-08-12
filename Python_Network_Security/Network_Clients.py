# Network Client test:


import socket

host = 'localhost' # 127.0.0.1 - This is the loop back interface
# The loop back interface only takes to the local machine, it can never be used to get off the local machine

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# What is the difference between TCP and UDP ? 


addr = (host, 5555)
mysock.connect(addr)

try:
    msg = b"Hi, this is a test\n"
    # Putting the 'b' in front of the string will turn the string into a byte array
    mysock.sendall(msg)
except socket.errno as e:
    print('Socket error', e)
finally:
    mysock.close()