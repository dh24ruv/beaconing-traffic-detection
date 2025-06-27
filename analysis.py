import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
from ipwhois import IPWhois

# Step 1: Load CSV
df = pd.read_csv("rich_traffic.csv")

# Step 2: Clean and convert data
df['frame.len'] = pd.to_numeric(df['frame.len'], errors='coerce').fillna(0)

# Step 3: Use only numeric columns for modeling
features = df[['frame.len']]

# Step 4: Train Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(features)

# Step 5: Predict anomalies and assign to new column
df['anomaly'] = model.predict(features)  # This line creates the column

# Step 6: Plot anomalies
plt.figure(figsize=(14, 7))
plt.scatter(df.index, df['frame.len'], c=(df['anomaly'] == -1), cmap='coolwarm', label='Anomaly')
plt.xlabel("Packet index")
plt.ylabel("Packet size (frame.len)")
plt.title("Anomaly Detection in Network Traffic")
plt.legend()
plt.show()

# Step 7: Print suspicious IPs (GeoIP Lookup)
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
