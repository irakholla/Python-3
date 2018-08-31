import socket
sock = socket.socket()
print('Waiting for connection', '\n')
sock.connect(('192.168.40.123', 9090))
sdata = input()
sock.send(sdata.encode('utf-8'))
fp = open("C:\\scripts\\screen.jpg", "wb")
while True:
    data = sock.recv(4096)
    fp.write(data)
    if not data:
        break
fp.close()
sock.close()



