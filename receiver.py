from vidstream import StreamingServer
import threading
print('waiting for screen....')
receiver = StreamingServer('192.168.0.103', 9999)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != "STOP":
    continue
receiver.stop_server()



