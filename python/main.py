from protector import RateLimiter, IPBlocker, log_event

def main():
    print("--- Protector Security Suite Starting ---")
    
    # 1. Test the Logger
    log_event("System", "Security suite initialized and testing imports.")

    # 2. Test the IP Blocker
    blocker = IPBlocker()
    test_ip = "192.168.1.100"
    blocker.block_ip(test_ip)
    
    if blocker.is_blocked(test_ip):
        print(f"SUCCESS: {test_ip} is successfully blocked.")

    # 3. Test the Rate Limiter
    limiter = RateLimiter(max_requests=2)
    user_id = "user_123"
    
    # Simulate requests
    for i in range(3):
        allowed = limiter.check_request(user_id)
        status = "Allowed" if allowed else "Blocked (Rate Limit Exceeded)"
        print(f"Request {i+1}: {status}")

    print("--- Test Complete ---")

if __name__ == "__main__":
    main()