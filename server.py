import time
import socket
import threading
import time_module

version_str = "HTTP/1.1 200 OK\n"
body_str = str()
header = {
    "Date": time_module.string_time(),
    "Server": "MH/0.01",
    "Content-Type": "text/html, charset=utf-8",
    "Content-Length": len(body_str),
    "Connection": "Keep-Alive",
    "Keep-Alive": "timeout=5, max=10"
}

x = open("body.html","r")
body_str = x.read()
x.close()
header["Content-Length"] = len(body_str)

header_str = ''.join(f"{k}: {v}\n"for k,v in header.items())
response = version_str+header_str+"\n"+body_str
response = response.encode()

SERVER = "192.168.0.102"
PORT = 6060
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def browser_handle(browser, addr):
    print(f"{addr} is connected....")
    recv = browser.recv(800).decode()
    present = time.time()
    print(recv)
    try:
        browser.send(response)
    except:
        recv = None
    while recv:
        recv = browser.recv(800).decode()
        now = time.time()
        if now-present>=5 or not recv:
            break
        print(recv)
        browser.send(response)
    browser.close()

def start():
    server.listen(100)
    while True:
        browser, addr = server.accept()
        thread = threading.Thread(target=browser_handle, args=(browser, addr))
        thread.start()
        count = threading.active_count()-1
        print(f"Connected Browser: {count}")

print("Server: MH/0.01\nServer is Running...")
start()