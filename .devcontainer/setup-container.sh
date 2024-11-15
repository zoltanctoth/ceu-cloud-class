#!/usr/bin/env bash
set -x
mkdir -p ~/.ssh
chmod 700 ~/.ssh

cat > ~/.ssh/config << 'EOL'
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 10
    TCPKeepAlive yes
EOL

chmod 600 ~/.ssh/config
