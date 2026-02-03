---
name: networking_concepts
description: OSI model, TCP/IP, protocols, packet analysis, and mobile networking concepts
---

# Networking Concepts Assistant

**Purpose:** Explain networking theory, protocols, and mobile computing concepts for MCN.

---

## OSI Model Reference

| Layer | Name         | PDU     | Function              | Protocols            |
| ----- | ------------ | ------- | --------------------- | -------------------- |
| 7     | Application  | Data    | User interface        | HTTP, FTP, SMTP, DNS |
| 6     | Presentation | Data    | Format, encryption    | SSL/TLS, JPEG, ASCII |
| 5     | Session      | Data    | Session management    | NetBIOS, RPC         |
| 4     | Transport    | Segment | End-to-end delivery   | TCP, UDP             |
| 3     | Network      | Packet  | Routing, addressing   | IP, ICMP, ARP        |
| 2     | Data Link    | Frame   | Node-to-node transfer | Ethernet, PPP, MAC   |
| 1     | Physical     | Bits    | Physical transmission | Cables, signals      |

---

## TCP/IP Model

| Layer          | OSI Equivalent | Key Protocols   |
| -------------- | -------------- | --------------- |
| Application    | 5, 6, 7        | HTTP, FTP, SMTP |
| Transport      | 4              | TCP, UDP        |
| Internet       | 3              | IP, ICMP        |
| Network Access | 1, 2           | Ethernet, Wi-Fi |

---

## Key Protocol Comparisons

### TCP vs UDP
| Feature     | TCP                       | UDP                    |
| ----------- | ------------------------- | ---------------------- |
| Connection  | Connection-oriented       | Connectionless         |
| Reliability | Guaranteed delivery       | Best effort            |
| Ordering    | Maintained                | Not guaranteed         |
| Speed       | Slower                    | Faster                 |
| Use Case    | Web, email, file transfer | Streaming, gaming, DNS |

---

## Mobile Networking Concepts

| Generation | Speed             | Key Features        |
| ---------- | ----------------- | ------------------- |
| 2G         | 14-64 Kbps        | Voice, SMS          |
| 3G         | 384 Kbps - 2 Mbps | Mobile internet     |
| 4G/LTE     | 100 Mbps - 1 Gbps | HD streaming, VoLTE |
| 5G         | 1-10 Gbps         | IoT, low latency    |

---

## Common Calculations

| Metric             | Formula                        |
| ------------------ | ------------------------------ |
| Bandwidth          | Data / Time                    |
| Latency            | RTT / 2                        |
| Throughput         | Actual data transferred / Time |
| Propagation Delay  | Distance / Speed               |
| Transmission Delay | Packet Size / Bandwidth        |

---

## Explanation Rules

- Use layer-by-layer analysis for protocol questions
- Show packet structure when explaining headers
- Include Wireshark filter examples where relevant
- Compare similar protocols explicitly
- Draw network diagrams using Mermaid when helpful
