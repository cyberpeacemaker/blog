---
created: 2026-07-07
tags: [dev, environment, moc]
type: hub
lang: en
status: published
---

# MOC - Dev Environment

Developer tooling: Git, Python, VS Code, testing, and environment setup.

## Setup
- [[docker-cs-claw-gemini-advice]] — hybrid local development with Docker-managed services

- [[env-setup]] — full dev environment setup (C, AI, cybersecurity)
- [[npm-node-domexception-deprecation]] — npm `node-domexception` deprecation warning triage
- [[timezone]] — timezone configuration
- [[YAML]] — YAML configuration files
- [[microsoft-store]] — Microsoft Store vs standalone installers for dev tools

## Windows, WSL, and Shells

- [[wsl-network-troubleshooting-dns-mirrored]] — Chinese WSL DNS, mirrored networking, proxy, firewall, and GitHub timeout checklist
- [[wsl-mtu]] — test, calculate, and persist WSL MTU values for VPN and corporate network issues
- [[wsl-conf-systemd-mtu]] — add an MTU boot command without overwriting WSL systemd support
- [[wsl-network-troubleshooting-mtu]] — diagnose WSL TCP timeouts when ping and DNS still work
- [[nics-claw-wsl]] — WSL-native clone, Conda, and VS Code workflow for NICS CLAW setup
- [[nics-claw-avoid-vmware]] — avoid adding VMware/Kali when WSL2, Docker Desktop, and VS Code match the team environment
- [[symantec-policy-location]] — verify and refresh Symantec Endpoint Protection policy serial numbers
- [[wsl-network-troubleshooting]] — WSL2 DNS, IPv6, mirrored networking, MTU, firewall, and proxy fixes
- [[wsl-ipv4-ipv6]] — prefer IPv4 in WSL when IPv6 routing causes curl and package-manager timeouts
- [[wsl-mirrored-cancel-wslconfig]] — roll back WSL mirrored networking to default NAT mode
- [[wsl-network-issue-antivirus-possible]] — Symantec SONAR and enterprise antivirus interference with WSL/dev tools
- [[vim-permission]] — save root-owned Linux files after Vim E45 readonly errors
- [[win-linux-crlf]] — convert Windows CRLF line endings before running shell scripts on Linux
- [[windows-sh-vs-powershell]] — why Linux .sh and systemd scripts do not run natively in PowerShell
- [[windows-sh-systemd-powershell]] — Linux Bash and systemd scripts versus native Windows PowerShell
- [[powershell-v5-v7]] — switch VS Code from Windows PowerShell 5 to PowerShell 7
- [[powershell-and-operator]] — alternatives to && in Windows PowerShell 5
- [[windows-file-permissions-icacls]] — chmod and icacls equivalents for sensitive file permissions

## Git

- [[canary-pattern]] — harmless secret-scanning canary string for hook and CI guardrail verification
- [[github-markdown-spacing]] — GitHub Markdown code fence failures from hidden spaces and list indentation
- [[github-ssh-gpgkey]] — GitHub SSH, HTTPS, PAT, and Credential Manager troubleshooting in WSL
- [[win11-git-clone-ssh]] — Windows 11 GitHub SSH clone setup with HTTPS fallback
- [[git-new-home]] — move an existing Git repo to a new GitHub remote while keeping history
- [[migrate-without-git]] — start a clean V2 project without carrying Git history
- [[fix-broken-cicd]] — handling broken CI/CD required checks
- [[git-squash-merge]] — GitHub squash merge review safety
- [[git-self-experience]] — Git and CI/CD review roadmap
- [[pr-auto-merge-github-action]] — daily triage PR auto-merge workflow plan
- [[github-action-flaws]] — Git hooks and GitHub Actions guardrail tradeoffs
- [[github-actions-sensitive-patterns]] — GitHub Secrets tradeoffs for CI sensitive-pattern scanning
- [[github-collaboration-pr-loop]] — issue, PR review, kanban, and CI loop for two-person teams
- [[github-collaboration]] — GitHub collaboration workflow for small teams
- [[github-collaboration-personal-organization-account]] — personal-account collaboration and organization tradeoffs
- [[github-hook-action]] — Git hooks vs GitHub Actions
- [[github-private-clone]] — private repo clone over SSH on Windows
- [[github-ssh]] — GitHub SSH setup on Windows PowerShell
- [[github-permission-ssh]] — SSH permission troubleshooting
- [[git-ssh-permission-denied]] — GitHub SSH publickey failures and HTTPS fallback
- [[git-issue-nuke]] — avoiding Git repository nuclear recovery
- [[git-recommended-roadmap]] — progressive Git learning roadmap
- [[git-learn]] — Microsoft Learn Git and GitHub study path

- [[git-best-practice]] — Git best practices
- [[git-pr-example]] — PR workflow example
- [[automation-pr-merge-policy]] — PR auto-merge, direct-to-main, and review-first automation patterns
- [[pr-auto-merge-policy-gh-pr-create]] — PR + auto-merge verdict for daily inbox triage automation
- [[git-post-merge-work-issue]] — recover commits pushed after a PR has already merged
- [[git-squash-and-merge]] — iterative commits with squash merge workflow
- [[agent-pr-squash-and-merge]] — PR auto-merge finish script for trusted daily inbox triage
- [[github-authentication]] — GitHub authentication
- [[github-organization]] — GitHub repo organization
- [[github-share-repo]] — sharing repos and collaborator access
- [[git-copied]] — Git push checklist (save, upload, .gitignore)
- [[git-nuclear]] — Git nuclear options
- [[git-other]] — miscellaneous Git notes
- [[git-bash]] — Git Bash on Windows
- [[gitkeep]] — .gitkeep pattern
- [[markdown-link-check-github-action]] — GitHub Action for Markdown link checks

## Python
- [[conda-install-option]] — choosing yes or no for Conda installer shell initialization
- [[conda-env-powershell]] — initialize Conda before creating environments from PowerShell
- [[miniconda-powershell-shortcut]] — dedicated Miniconda PowerShell shortcut
- [[conda-system-python]] — Conda isolation and system Python guardrails
- [[conda-uv-pixi]] — Conda, uv, and pixi toolchain tradeoffs
- [[powershell-brackets]] — PowerShell array syntax for path checks
- [[conda-miniconda-anaconda]] — Conda, Miniconda, and Anaconda overview
- [[conda-powershell]] — Conda in PowerShell on Windows

- [[pyproject]] — pyproject.toml setup
- [[python-import]] — Python import patterns
- [[python-venv]] — Python venv
- [[python-venv-v2]] — Python venv (updated)
- [[conda-necessary]] — when Conda is necessary
- [[conda-miniconda]] — Conda, Miniconda, and Anaconda overview
- [[uv-conda]] — choosing uv for PoC work and Conda for GPU-heavy AI
- [[python-cpp-environment]] — Python + C++ environment
- [[python-test-module-path]] — test module paths
- [[dry-run-pytest]] — pytest dry-run patterns
- [[requirements]] — requirements management
- [[build-graph]] — build dependency graph
- [[requirement-naming]] — requirement naming conventions
- [[strict-json-syntax]] — strict JSON syntax
- [[win5-strip-quote]] — Windows quote stripping
- [[bracket-paste]] — bracket paste
- [[powershell-execution-policy]] — PowerShell execution policy

## VS Code / Cursor

- [[vscode-custom-visual-text]] — customize VS Code editor typography, Markdown syntax colors, preview CSS, and extensions
- [[vscode-custom-visual-template]] — language-specific settings for visually separating plaintext and Markdown files
- [[vscode-close-http-server]] — stop Python HTTP servers cleanly from the VS Code integrated terminal
- [[vscode-fold-markdown-vs-code]] — Markdown folding behavior versus programming-language folding in VS Code
- [[vscode-blockquote-lines]] — add Markdown blockquote markers to many lines with regex or multi-cursor editing
- [[vscode-gitlens-get-started]] — GitLens getting started
- [[vscode-extensions-starter-pack]] — VS Code extensions starter pack
- [[git-blame-timeline-gitlens]] — Git blame, Timeline, and GitLens workflows

- [[vscode-tips]] — VS Code tips
- [[vscode-tips-v2]] — VS Code tips (updated)
- [[vscode-PR]] — VS Code PR workflow
- [[setting-split]] — settings split
- [[vscode-pretty]] — VS Code prettify
- [[markdon-preview]] — default markdown preview in VS Code
- [[vscode-open-view]] — open .md files in preview by default
- [[vscode-toggle-view]] — Markdown preview shortcuts
- [[automatically-update-internal-link]] — Markdown link updates when moving files
- [[vscode-new-note-template]] — VS Code/Cursor options for creating templated Inbox notes

## Testing

- [[playwright]] — Playwright E2E testing
- [[jest]] — Jest unit testing
- [[smoke]] — smoke testing
- [[boundary-edge]] — boundary/edge testing

## Related

- [[MOC - Claude & Cursor]] — AI-assisted development
- [[My Stack]] — full tool inventory
