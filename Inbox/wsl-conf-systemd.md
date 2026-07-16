---
created: 2026-07-16 20:07
updated: 2026-07-16 20:07
tags: []
type: reference
lang: en
status: draft
---
Yes, that is completely fine! Having `systemd=true` under `[boot]` is very common—it just means you've enabled systemd support so you can run background services (like Docker, microk8s, or system services) inside Kali Linux.

To add the permanent MTU fix, you **do not** want to overwrite that line or create a duplicate `[boot]` section. Instead, you just add the MTU command right underneath it.

### Your Updated `wsl.conf`

Open the file again with `sudo nano /etc/wsl.conf` and update it so it looks exactly like this:

Ini, TOML

```
[boot]
systemd=true
command = "ip link set dev eth0 mtu 1350"
```

_(Feel free to swap `1350` for whatever optimal MTU you calculated in the previous step)._

### What to do next:

1. Save the file in nano (`Ctrl+O`, then `Enter`, then `Ctrl+X`).
    
2. Open Windows PowerShell or Command Prompt on your host machine and restart WSL to apply the changes:
    
    PowerShell
    
    ```
    wsl --shutdown
    ```
    
3. Re-open your Kali terminal and verify it worked by running:
    
    Bash
    
    ```
    ip link show eth0
    ```
    

Did the MTU adjustment resolve the connection issues you were experiencing?

