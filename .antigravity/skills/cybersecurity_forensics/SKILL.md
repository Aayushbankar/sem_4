---
name: cybersecurity_forensics
description: Security concepts, digital forensics, Kali Linux tools, and incident response
---

# Cybersecurity & Forensics Assistant

**Purpose:** Explain security concepts, forensic procedures, and guide CSDF practicals.

---

## Security Fundamentals

### CIA Triad
| Principle       | Definition                         | Threats               | Controls                   |
| --------------- | ---------------------------------- | --------------------- | -------------------------- |
| Confidentiality | Data accessible only to authorized | Eavesdropping, theft  | Encryption, access control |
| Integrity       | Data is accurate and unaltered     | Tampering, corruption | Hashing, checksums         |
| Availability    | Systems accessible when needed     | DoS, failures         | Redundancy, backups        |

---

## Attack Categories

| Category           | Examples                  | Defense                |
| ------------------ | ------------------------- | ---------------------- |
| Network            | DDoS, MITM, Sniffing      | Firewalls, encryption  |
| Application        | SQLi, XSS, CSRF           | Input validation, WAF  |
| Social Engineering | Phishing, pretexting      | Training, verification |
| Malware            | Virus, ransomware, trojan | AV, sandboxing         |

---

## Digital Forensics Process

```
1. Identification → 2. Preservation → 3. Collection → 4. Examination → 5. Analysis → 6. Presentation
```

| Phase          | Key Actions               |
| -------------- | ------------------------- |
| Identification | Scope, evidence sources   |
| Preservation   | Chain of custody, imaging |
| Collection     | Forensic copies, hashing  |
| Examination    | Data extraction, recovery |
| Analysis       | Timeline, correlation     |
| Presentation   | Report, court-ready docs  |

---

## Kali Linux Tools Reference

| Tool       | Purpose           | Example Command                    |
| ---------- | ----------------- | ---------------------------------- |
| nmap       | Port scanning     | `nmap -sV -sC target`              |
| Wireshark  | Packet capture    | GUI or `tshark -i eth0`            |
| hashcat    | Password cracking | `hashcat -m 0 hash.txt wordlist`   |
| volatility | Memory forensics  | `volatility -f dump.raw imageinfo` |
| autopsy    | Disk forensics    | GUI-based analysis                 |
| steghide   | Steganography     | `steghide extract -sf image.jpg`   |
| john       | Password cracking | `john --wordlist=rockyou.txt hash` |
| binwalk    | Firmware analysis | `binwalk -e firmware.bin`          |

---

## Evidence Handling

| Principle        | Description                              |
| ---------------- | ---------------------------------------- |
| Chain of Custody | Document who handled evidence, when, why |
| Write Blocking   | Prevent modification during imaging      |
| Hashing          | Verify integrity (MD5, SHA-256)          |
| Documentation    | Photograph, log every action             |

---

## Explanation Rules

- Always emphasize legal and ethical boundaries
- Include exact command syntax with explanations
- Show expected output format
- Reference CVE numbers for known vulnerabilities
- Distinguish between offensive and defensive context
