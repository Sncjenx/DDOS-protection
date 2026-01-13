from ipaddress import ip_address
import time

class IPBlocker:
    def __init__(self, block_duration: int = 300):
        self.block_duration = block_duration
        self.blocked_ips = {}

    # Inside ip_blocker.py, change your method name to match this:
    def block_ip(self, ip_address):
        self.blocked_ips[ip_address] = True  # or your specific logic
        print(f"IP {ip_address} has been blocked.")

    def is_blocked(self, ip: str) -> bool:
        if ip not in self.blocked_ips:
            return False

        blocked_time = self.blocked_ips[ip]
        if time.time() - blocked_time > self.block_duration:
            del self.blocked_ips[ip]
            return False

        return True
