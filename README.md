

🛡️ Updated Documentation (v1.1.0)
Protector Security Suite Hybrid Python Engine + C++ GUI Dashboard

A lightweight defensive system designed to protect local servers from request flooding. This version introduces a high-speed C++ interface to monitor the Python-based protection logic in real-time.

✨ Key Features

IP-Based Rate Limiting (Python): Controls the flow of incoming requests based on configurable time windows.

Automated IP Blocking (Python): Temporarily restricts abusive IP addresses.

Native Dashboard (C++): A high-performance GUI built with Qt for real-time monitoring.

Centralized Configuration: All security thresholds (request limits, block duration) are managed in config.py.

Detailed Logging: Tracks all security events to security_log.txt.

📁 Updated Project Structure
This layout keeps your "brain" (Python) and "face" (C++) separated for a professional look.

Plaintext

ddos-protection-python/
│
├── protector/ (Python Core)
│   ├── __init__.py      # Package entry point
│   ├── rate_limiter.py  # Request frequency logic
│   ├── ip_blocker.py    # Blocking mechanism
│   └── logger.py        # Event recording
│
├── gui_cpp/ (C++ Dashboard)
│   ├── src/
│   │   └── main.cpp     # Qt GUI logic
│   └── CMakeLists.txt   # Build configuration
│
├── example_server.py    # Local HTTP server test
├── config.py            # Global settings
├── README.md            # Project documentation
└── LICENSE              # MIT License
