
## all help is welcome ##

🛡️ Protector Security Suite (v1.1.0)
Hybrid Python Engine + C++ GUI Dashboard

A defensive security tool designed to protect local servers from request flooding. This version introduces a high-speed C++ interface to monitor the Python-based protection logic in real-time. 
+1

✨ Features

IP-Based Rate Limiting (Python): Controls the flow of incoming requests based on configurable time windows.


Automated IP Blocking (Python): Temporarily "jails" abusive IP addresses.

High-Performance Dashboard (C++): A native GUI built with Qt for monitoring system status without slowing down the core engine.


Centralized Configuration: All security thresholds are managed in one config.py file.


Detailed Logging: Tracks all blocks and system events to security_log.txt.

📁 Updated Project Structure
This new structure separates your high-speed UI code from your core logic.

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
├── requirements.txt     # Python dependencies [cite: 2]
├── README.md            # Project documentation 
└── LICENSE              # MIT License
