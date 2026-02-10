import pandas as pd

url = "https://www.football-data.co.uk/mmz4281/2324/E0.csv"

print("Downloading data...")

df = pd.read_csv(url)

df.to_csv("data/premier_league.csv", index = False)

print(f"✅ Success! Downloaded {len(df)} matches")
print(f"✅ Saved to data/premier_league.csv")