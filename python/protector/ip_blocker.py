import time

class IPBlocker:
    def __init__(self, block_duration: int):
        self.block_duration = block_duration
        self.blocked_ips = {}

    def block(self, ip: str):
        self.blocked_ips[ip] = time.time()

    def is_blocked(self, ip: str) -> bool:
        if ip not in self.blocked_ips:
            return False

        blocked_time = self.blocked_ips[ip]
        if time.time() - blocked_time > self.block_duration:
            del self.blocked_ips[ip]
            return False

        return True
