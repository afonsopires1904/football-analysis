import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("data/premier_league.csv")

#Total remates enquadrados casa e fora
df_casa = df[['HomeTeam', 'FTHG', 'HST']].rename(columns={
    "HomeTeam": "Team",
    "FTHG": "Goals",
    "HST": "ShotsOnTarget"
})

df_fora = df[['AwayTeam', 'FTAG', 'AST']].rename(columns={
    "AwayTeam": "Team",
    "FTAG": "Goals",
    "AST": "ShotsOnTarget"
})

#CASA E FORA
df_casa_fora = pd.concat([df_casa, df_fora])

#Agrupar por equipa e somar "Goals" e "ShotsOnTarget"
stats_goals_goals_ST = df_casa_fora.groupby("Team")[["Goals", "ShotsOnTarget"]].sum()

#EFICIÊNCIA ;; Eficiencia = (GOLOS / REMATES ENQUADRADOS) * 100

# Calcular E adicionar ao DataFrame
stats_goals_goals_ST['Efficiency'] = (
    stats_goals_goals_ST["Goals"] / 
    stats_goals_goals_ST["ShotsOnTarget"]
) * 100

top5 = stats_goals_goals_ST.sort_values("Efficiency", ascending=False).head(5)

#GRAFICO DISPERSAO - REMATES vs GOLOS

plt.figure(figsize=(12,8))

# x = remates ; y = golos 
x = stats_goals_goals_ST["ShotsOnTarget"]
y = stats_goals_goals_ST["Goals"]

#LINHA DE TENDÊNCIA
coeficientes = np.polyfit(x, y, 1)
m = coeficientes[0]
b = coeficientes[1]

linha_x = np.array([x.min(), x.max()])
linha_y = m * linha_x + b

#Scatter
plt.scatter(x, y, s=100, alpha=0.6, color='blue', label='Teams')

#LINHA DE TENDÊNCIA PLOTTED
plt.plot(linha_x, linha_y, color = "red", linewidth = 2, linestyle = "--", label=f"Trend: y={m:.2f}x + {b:.0f}")

#Nomes equipas
for equipa in stats_goals_goals_ST.index:
    x_pos = stats_goals_goals_ST.loc[equipa, "ShotsOnTarget"]
    y_pos = stats_goals_goals_ST.loc[equipa, "Goals"]
    
    plt.annotate(
        equipa,
        (x_pos, y_pos),
        xytext=(5, 5),  
        textcoords='offset points',
        fontsize=7,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3)
    )

#EFICIÊNICA NO PLOT
top5_eff = "Efficiency: \n"
for equipa in top5.index:
    eficiencia = top5.loc[equipa, "Efficiency"]

    top5_eff += f"{equipa}: {eficiencia:.1f}%\n"

plt.text(0.05, 0.95, top5_eff,
         transform=plt.gca().transAxes,
         verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor = "lightgreen", alpha=0.8))

plt.xlabel("Shots On Target")
plt.ylabel("Goals")
plt.title("Shots on Target vs Goals - Premier League 2023/24")

plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)
plt.tight_layout()


plt.savefig("outputs/graph/shots_vs_goals.png", dpi=300, bbox_inches = "tight")


plt.show()

