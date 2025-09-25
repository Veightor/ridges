"""
Constants for sandbox operations.
"""

# Docker image names
SANDBOX_DOCKER_IMAGE = "sandbox-image"
PROXY_DOCKER_IMAGE = "sandbox-proxy-image"

# Network configuration
SANDBOX_NETWORK_NAME = "sandbox-network"
PROXY_CONTAINER_NAME = "sandbox_proxy"

# Resource limits
SANDBOX_MAX_RAM_USAGE = 1073741824  # 1 GB RAM limit in bytes
SANDBOX_MAX_RUNTIME = 300  # 5 minutes timeout in seconds

# File paths in sandbox
MAIN_FILE = "main.py"
SANDBOX_MAIN_FILE = "/sandbox/main.py"
SANDBOX_INPUT_FILE = "/sandbox/input.json"
SANDBOX_OUTPUT_FILE = "/sandbox/output.json"

# Directory paths in sandbox
SANDBOX_SOURCE_DIR = "/sandbox/src"
SANDBOX_REPO_DIR = "/sandbox/repo"
SANDBOX_DIR = "/sandbox"
