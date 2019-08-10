# The socket library, will allow us to lookup IP or hostname

import socket
print(socket.gethostbyaddr('8.8.8.8'))
print(socket.gethostbyaddr('158.57.12.43')) # Coned DNS 
print(socket.gethostbyname('www.google.com'))