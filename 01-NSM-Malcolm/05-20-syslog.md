

### How Syslog Works

Syslog operates on a client-server model:

* **The Client (Sender):** The device or application that generates the log message (e.g., a router noticing a failed login attempt).
* **The Server (Receiver/Collector):** A centralized machine that receives, categorizes, and stores the log messages from multiple clients.

These messages are typically sent over a network using port 514 (UDP) or port 6514 (TCP for secure, encrypted delivery).

---

### The Anatomy of a Syslog Message

When a device sends a syslog message, it tags the data with two main identifiers so the server knows exactly how to handle it:

**1. Facility (Who sent it?)**
This indicates the type of system or application that generated the log. Common facilities include:

* `auth` or `authpriv` (Security/authentication events)
* `kern` (Kernel messages)
* `mail` (Mail systems)
* `cron` (Scheduled tasks)

**2. Severity (How bad is it?)**
This tells you how urgent the message is. There are 8 standard severity levels:

| Level | Name | Description |
| --- | --- | --- |
| **0** | Emergency | System is unusable (highest priority). |
| **1** | Alert | Action must be taken immediately. |
| **2** | Critical | Critical conditions (e.g., hard drive failure). |
| **3** | Error | Error conditions. |
| **4** | Warning | Warning conditions. |
| **5** | Notice | Normal but significant conditions. |
| **6** | Informational | General information messages. |
| **7** | Debug | Messages used for troubleshooting (lowest priority). |

---

### Why is Syslog Important?

* **Centralized Troubleshooting:** Instead of logging into 50 different servers to figure out why an application crashed, you can search for the error in one central syslog server.
* **Security & Auditing:** Hackers often try to delete local logs to cover their tracks. If logs are instantly forwarded to a remote syslog server, you preserve the evidence.
* **Alerting:** You can configure a syslog server to instantly email or text you if it receives a Severity 0 (Emergency) or Severity 1 (Alert) message.

### Modern Implementations

The original syslog protocol was created in the 1980s. Today, most modern Linux distributions use upgraded, feature-rich versions of the daemon like **rsyslog** or **syslog-ng**, which support better filtering, TCP connections, and encryption, while still remaining compatible with the original syslog standard.