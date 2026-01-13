import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_requests=5, window_seconds=60):
        self.max_requests = max_requests
        self.window = window_seconds
        self.requests = defaultdict(list)

    def check_request(self, user_id: str) -> bool:
        """
        Checks if a user/IP is allowed to make a request based on the rate limit.
        """
        now = time.time()

        # 1. Clean up: Keep only requests inside the time window
        self.requests[user_id] = [
            t for t in self.requests[user_id]
            if now - t < self.window
        ]

        # 2. Check: Is the user over the limit?
        if len(self.requests[user_id]) >= self.max_requests:
            return False

        # 3. Register: Add the current request timestamp
        self.requests[user_id].append(now)
        return True
