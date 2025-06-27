import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

df = pd.read_csv('rich_traffic.csv')

df = df.dropna(subset=['ip.src', 'ip.dst', 'frame.len'])

df[['tcp.srcport', 'tcp.dstport']] = df[['tcp.srcport', 'tcp.dstport']].fillna(0)

df['frame.time_epoch'] = pd.to_numeric(df['frame.time_epoch'], errors='coerce')
df['frame.len'] = pd.to_numeric(df['frame.len'], errors='coerce')
df['tcp.srcport'] = pd.to_numeric(df['tcp.srcport'], errors='coerce')
df['tcp.dstport'] = pd.to_numeric(df['tcp.dstport'], errors='coerce')

df = df.dropna()

X = df[['frame.len', 'tcp.srcport', 'tcp.dstport']]

model = IsolationForest(contamination=0.05, random_state=42)
df['anomaly'] = model.fit_predict(X)

plt.figure(figsize=(10, 5))
plt.scatter(df.index, df['frame.len'], c=df['anomaly'].map({1: 'blue', -1: 'red'}))
plt.title("Anomaly Detection in Network Traffic")
plt.xlabel("Packet index")
plt.ylabel("Packet size (frame.len)")
plt.legend(['Normal', 'Anomaly'])
plt.grid(True)
plt.tight_layout()
plt.show()

from ipwhois import IPWhois

suspicious_ips = df[df['anomaly'] == -1]['ip.src'].dropna().unique()

for ip in suspicious_ips[:5]:  # limit to top 5 for speed
    try:
        info = IPWhois(ip).lookup_rdap()
        print(f"IP: {ip} — Country: {info['network']['country']}, Org: {info['network']['name']}")
    except:
        print(f"IP: {ip} — Lookup failed")
