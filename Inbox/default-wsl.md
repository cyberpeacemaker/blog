---
created: 2026-07-21 17:07
updated: 2026-07-21 17:07
tags: []
type: reference
lang: en
status: draft
---
你的判斷對了：**不是 Ubuntu 的 Docker 壞掉，是 VS Code 打錯 distro。**

## 根因

從 log 可以直接看出：

```text
wsl -d kali-linux -e ...
docker version --format {{json .}}
→ The command 'docker' could not be found in this WSL 2 distro
```

而你的 WSL 清單是：

| Distro | 狀態 |
|---|---|
| `kali-linux` | **Default** ← Dev Containers 預設打這裡 |
| `Ubuntu-24.04` | Docker Engine 裝好且驗證通過 |
| `docker-desktop` | Docker Desktop 殘留 |

勾了 **Execute In WSL** 後，若沒指定 distro，就會用 **WSL 預設發行版**。你預設是 kali，kali 裡沒有 Docker Engine，所以失敗；Ubuntu 那邊其實是好的。

## 怎麼修（二選一）

**做法 A（建議，對齊 onboarding）** — 把預設改成 Ubuntu：

```powershell
wsl --set-default Ubuntu-24.04
wsl -l -v   # 確認 (Default) 在 Ubuntu-24.04
```

然後完全關掉 VS Code 再開，重跑 **Clone Repository in Container Volume**。新 log 應出現 `wsl -d Ubuntu-24.04`，而不是 `kali-linux`。

**做法 B** — 保留 kali 當預設，只讓 Dev Containers 用 Ubuntu：

VS Code 設定搜尋 `executeInWSLDistro`，設成：

```text
Ubuntu-24.04
```

（同時維持 `Execute In WSL` 勾選。）

## 關於「kali / Ubuntu 混在一起」

沒有真的混成一個系統，是 **VS Code 選錯了要進的那個 WSL**。兩邊各自獨立；你手動 `wsl -d Ubuntu-24.04` 時 Docker 正常，就是這個意思。

另外 log 裡還會去啟動 `Docker Desktop.exe`——那是找不到 docker 後的 fallback。這份指南要用的是 Ubuntu 內的 **Docker Engine**，不要對 Ubuntu 開 Desktop 的 WSL integration（開了反而會跟 bootstrap 打架）。本機若不需要 Desktop，之後再卸載也行。

先做做法 A，再貼一段新的 Dev Containers log 開頭（有沒有 `wsl -d Ubuntu-24.04`）就能確認是否過關。

