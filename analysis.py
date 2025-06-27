import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
from ipwhois import IPWhois

df = pd.read_csv("rich_traffic.csv")

df['frame.len'] = pd.to_numeric(df['frame.len'], errors='coerce').fillna(0)

features = df[['frame.len']]

model = IsolationForest(contamination=0.05, random_state=42)
model.fit(features)

df['anomaly'] = model.predict(features)  

plt.figure(figsize=(14, 7))
plt.scatter(df.index, df['frame.len'], c=(df['anomaly'] == -1), cmap='coolwarm', label='Anomaly')
plt.xlabel("Packet index")
plt.ylabel("Packet size (frame.len)")
plt.title("Anomaly Detection in Network Traffic")
plt.legend()
plt.show()

print("\n🔎 Suspicious IP Origins:\n")
suspicious_ips = df[df['anomaly'] == -1]['ip.src'].dropna().unique()

for ip in suspicious_ips[:10]:
    try:
        obj = IPWhois(ip)
        res = obj.lookup_rdap()
        country = res['network']['country']
        org = res['network']['name']
        print(f"🟥 IP: {ip} | Country: {country} | Org: {org}")
    except Exception as e:
        print(f"❌ Couldn't lookup {ip}: {e}")
