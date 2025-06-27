# 🛰️ Network Beaconing & Anomaly Detection using Machine Learning

This project applies machine learning to detect **beaconing patterns** and **anomalies** in network traffic captured via `.pcap` files. Beaconing — a telltale sign of malware or command-and-control (C2) channels — involves repeated, periodic communication with external IPs. This tool automates detection and visualization of such suspicious behaviors using Isolation Forest and traffic analysis.

---

## 🔍 What This Project Detects

- 📡 **Beaconing**: Repeated packets to the same destination at fixed intervals
- 🧨 **Outlier Behavior**: Abnormal packet lengths, unusual ports, rare IPs
- 🌍 **Suspicious IP Origins**: Attribution using WHOIS and ASN data
- 📈 **Visual Evidence**: Time-series plots of detected anomalies

---

<img width="1210" alt="image" src="https://github.com/user-attachments/assets/3b1c9ee9-de9e-48a3-878f-4657cd7abd20" />


---

## ⚙️ Features

- ✅ **PCAP to CSV conversion** using `tshark`
- 📊 **Feature extraction**: IPs, ports, timestamps, packet sizes
- 🧠 **Anomaly detection** using Isolation Forest
- 🌍 **IP attribution** using WHOIS and IPWhois
- 📈 **Visualization** using Matplotlib
- 🔐 Focused on integrating **data science into cybersecurity**

---

## 🛠️ Tech Stack

- Python 3.12
- pandas, scikit-learn, matplotlib
- tshark (Wireshark CLI)
- ipwhois

## 🧠 Techniques Used

- `tshark` to extract raw packet features from `.pcap` files
- `pandas` for data cleaning & timestamp processing
- `IsolationForest` to detect outliers in packet behavior
- `ipwhois` to attribute suspicious IPs to organizations (Google, Amazon, Cloudflare, etc.)
- `matplotlib` for plotting anomalies over time
---

## 📂 Project Structure

network-traffic-analyzer/
├── analysis.py # ML model + anomaly analysis
├── process_traffic.py # Optional: tshark extractor
├── rich_traffic.csv # Output data from PCAP
├── beacon_mac.pcap # Sample PCAP file
└── README.md

## 🚀 Installation & Setup

### 1. Clone Repository

git clone https://github.com/dh24ruv/network-traffic-analyzer.git
cd network-traffic-analyzer

2. Install tshark

brew install wireshark

# How to Use
Step 1: Extract CSV from PCAP

tshark -r beacon_mac.pcap -T fields \
  -e frame.time_epoch -e ip.src -e ip.dst \
  -e frame.len -e tcp.srcport -e tcp.dstport \
  -E header=y -E separator=, > rich_traffic.csv

Step 2: Run the Analysis

python analysis.py

# Example Terminal Output

Suspicious IP Origins:

🟥 IP: 8.8.8.8           | Org: GOGL
🟥 IP: 54.185.38.139     | Org: AMAZO-ZPDX7
🟥 IP: 162.159.192.1     | Org: CLOUDFLARENET
❌ Private IPs skipped (RFC 1918): 172.16.10.x
