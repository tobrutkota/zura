import socket
import socks

# Konfigurasi proxy SOCKS5 (GANTI dengan proxy yang Ayah punya)
PROXY_IP = "149.102.250.97"
PROXY_PORT = 9999

# Pool mining tujuan
POOL_HOST = "us.vipor.net"
POOL_PORT = 5040

# Buat socket pakai SOCKS5
socks.set_default_proxy(socks.SOCKS5, PROXY_IP, PROXY_PORT)
socket.socket = socks.socksocket

# Connect ke pool lewat proxy
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((POOL_HOST, POOL_PORT))

print(f"✅ Terhubung ke {POOL_HOST}:{POOL_PORT} lewat {PROXY_IP}:{PROXY_PORT}")

# Loop buat teruskan data mining
while True:
    data = s.recv(4096)
    if not data:
        break
    print(f"📩 Data diterima: {data}")
    s.sendall(data)

s.close()
