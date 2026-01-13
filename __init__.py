"""
protector package

Defensive utilities for rate limiting, IP blocking,
and basic abuse protection.
"""

from .rate_limiter import RateLimiter
from .ip_blocker import IPBlocker
from .logger import log_event

__all__ = [
    "RateLimiter",
    "IPBlocker",
    "log_event",
]

__version__ = "0.1.0"
