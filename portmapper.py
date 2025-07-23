# PortMapper by KRISHNA 🛰️
import socket
import threading
import ipaddress
from datetime import datetime

print("""
   ____            _   __  __
  |  _ \ ___  _ __| |_|  \/  | __ _ _ __
  | |_) / _ \| '__| __| |\/| |/ _` | '_ \\
  |  __/ (_) | |  | |_| |  | | (_| | | | |
  |_|   \___/|_|   \__|_|  |_|\__,_|_| |_|  by KRISHNA

  🔍 Advanced TCP Port Scanner
""")

# Common ports & banners
common_ports = {
    21: 'FTP',
    22: 'SSH',
    23: 'TELNET',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    139: 'NetBIOS',
    143: 'IMAP',
    443: 'HTTPS',
    3306: 'MySQL',
    8080: 'HTTP-ALT'
}

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                banner = common_ports.get(port, "Unknown Service")
                print(f"[OPEN] {ip}:{port} ({banner})")
                with open("portmapper_log.txt", "a") as log:
                    log.write(f"{ip}:{port} ({banner})\n")
    except Exception:
        pass

def scan_host(ip, ports):
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(ip, port))
        thread.start()

def main():
    target = input("🌐 Enter target IP or CIDR (e.g. 192.168.1.1 or 192.168.1.0/24): ").strip()
    port_range = input("🔢 Enter port range (default 1-100): ").strip()
    ports = range(1, 101) if not port_range else range(*map(int, port_range.split("-")))

    print(f"\n📅 Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    try:
        ip_list = [str(ip) for ip in ipaddress.IPv4Network(target, strict=False)]
        for ip in ip_list:
            print(f"\n🎯 Scanning host: {ip}")
            scan_host(ip, ports)
    except ValueError:
        print("❌ Invalid IP or CIDR format.")

if __name__ == "__main__":
    main()
