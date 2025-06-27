# 🛡️ Network Traffic Anomaly Detection using Machine Learning

This project analyzes `.pcap` files captured from network traffic to identify anomalies using unsupervised machine learning models like Isolation Forest. It helps detect unusual patterns that might indicate malicious behavior, high traffic spikes, or protocol misuse.

## 📁 Features

- ✅ PCAP Parsing using `tshark`
- 📊 Feature Extraction (IP, Port, Packet Size, Timestamp)
- 🤖 Anomaly Detection using `IsolationForest`
- 🌐 WHOIS Lookup for Suspicious IPs
- 📈 Matplotlib Visualization

## 🧪 Example Output

![anomaly_detection](./anomaly_plot.png)

## 📦 Installation

```bash
pip install -r requirements.txt
