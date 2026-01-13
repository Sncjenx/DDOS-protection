from http.server import BaseHTTPRequestHandler, HTTPServer
from protector.rate_limiter import RateLimiter
from protector.ip_blocker import IPBlocker
from protector.logger import log_event
import config


rate_limiter = RateLimiter(
    max_requests=config.MAX_REQUESTS,
    window_seconds=config.WINDOW_SECONDS
)

ip_blocker = IPBlocker(
    block_duration=config.BLOCK_DURATION
)

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        ip = self.client_address[0]

        if ip_blocker.is_blocked(ip):
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"IP temporarily blocked")
            return

        if not rate_limiter.is_allowed(ip):
            ip_blocker.block(ip)
            log_event(f"Blocked IP due to abuse: {ip}")

            self.send_response(429)
            self.end_headers()
            self.wfile.write(b"Too many requests")
            return

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Request accepted")


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8080), RequestHandler)
    print("🛡️ Protection server running on http://localhost:8080")
    server.serve_forever()
