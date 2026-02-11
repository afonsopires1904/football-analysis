import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("data/premier_league.csv")


#Total golos por equipa

df_casa = df[['HomeTeam', 'FTHG', 'HST']].rename(columns={
    "HomeTeam": "Team",
    "FTHG": "Goals",
})

df_fora = df[['AwayTeam', 'FTAG', 'AST']].rename(columns={
    "AwayTeam": "Team",
    "FTAG": "Goals",
})

df_total = pd.concat([df_casa, df_fora], ignore_index=True)
top_10_golos = (df_total.groupby("Team")["Goals"]
                .sum()
                .reset_index()
                .sort_values(by= "Goals", ascending=False)
                .head(10))


plt.figure(figsize = (12, 8))

# Criar as barras horizontais
# Usa [::-1] para que o 1º lugar fique no topo
bars = plt.barh(top_10_golos["Team"][::-1], top_10_golos["Goals"][::-1], color='skyblue')

x = top_10_golos["Goals"]
y = top_10_golos["Team"]


plt.bar_label(bars, padding=5, fontweight='bold')
plt.xlabel("Total Goals Scored")
plt.ylabel("Team")
plt.title("TOP 10 Teams - Total Goals Scored")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()


plt.savefig("outputs/graph/top_team_scorers.png", dpi=300, bbox_inches = "tight")


plt.show()

