def screen(): # создаем функцию screen
    from PIL import ImageGrab # импортируем из библиотеки PIL функции ImageGrab
    global img # объявляем глобальыне перменные
    img = ImageGrab.grab() # делаем скриншот рабочего стола
    img.save("E:\\screen.jpg", "JPEG", quality=1200)  # сохраняем скриншот (новый автоматически заменит старый)
    return img # возвращаем переменную со скрином
import socket
print('Waiting for connection', '\n')
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
print('Connected:', addr)
while True:
    data = conn.recv(4096)
    cdata = data.decode('utf-8')
    print('Data: ', cdata)
    if cdata == 'screen':
        screen()
        conn.send(open('E:\\screen.jpg', 'rb').read())
        break
    if not data:
        break
conn.close()