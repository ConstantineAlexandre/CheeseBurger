#!/bin/bash

# Get the path of CheeseBurger.py
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SCRIPT_PATH="$SCRIPT_DIR/CheeseBurger.py"

# Change the CheeseBurger.py file to executable
chmod +x "$SCRIPT_PATH"

# Create a symbolic link in /usr/local/bin
ln -sf "$SCRIPT_PATH" /usr/local/bin/CheeseBurger

echo "CheeseBurger has been successfully installed. You can now run it with the 'CheeseBurger' command in the terminal."