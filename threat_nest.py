"""
Project Threat Nest: concise cross-platform security helper.
Provides stub for threat detection and basic data hiding using base64.
"""

import base64
import platform


def protect():
    """Simulate threat detection; stub for future enhancements."""
    print(f"Protecting on {platform.system()}...")


def hide_data(data: bytes) -> bytes:
    """Hide data using base64 encoding."""
    return base64.b64encode(data)


def reveal_data(hidden: bytes) -> bytes:
    """Reveal data by decoding base64."""
    return base64.b64decode(hidden)


if __name__ == "__main__":
    protect()
    secret = b"secret"
    hidden = hide_data(secret)
    print("Hidden:", hidden)
    print("Revealed:", reveal_data(hidden))
