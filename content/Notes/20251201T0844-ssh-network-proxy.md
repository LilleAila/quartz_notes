---
id: 20251201T0844-ssh-network-proxy
aliases:
  - ssh network proxy
tags: []
date: "2025-12-01"
title: ssh network proxy
---

#linux [[20240901T0613-linux|linux]]

# ssh network proxy

Can use something like this to create a `socks5` proxy at localhost, then launch a chromium browser using this:

```sh
#!/bin/bash

SSH_HOST="oci"
SOCKS_PORT=1080
CHROMIUM="/Applications/Chromium.app/Contents/MacOS/Chromium"

ssh -D "$SOCKS_PORT" -C -N "$SSH_HOST" &
SSH_PID=$!

cleanup() {
    kill "$SSH_PID" 2>/dev/null
}
trap cleanup EXIT INT TERM

"$CHROMIUM" --proxy-server="socks5://localhost:$SOCKS_PORT"
```
