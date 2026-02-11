import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

df = pd.read_csv("data/premier_league.csv")

#TOP 5 EQUIPAS VITORIAS

#VITORIAS EM CASA
df_win_home = df[["HomeTeam", "FTR"]].copy()
df_win_home["Win"] = (df_win_home["FTR"] == "H").astype(int)
df_win_home = df_win_home.rename(columns={"HomeTeam":"Team"})

#VITORIAS FORA
df_win_away = df[['AwayTeam', 'FTR']].copy()
df_win_away['Win'] = (df_win_away['FTR'] == 'A').astype(int)
df_win_away = df_win_away.rename(columns={"AwayTeam": "Team"})

#Concatenar e agrupar
df_total = pd.concat([df_win_home[['Team', 'Win']], df_win_away[['Team', 'Win']]], ignore_index=True)

top_5_wins = (df_total.groupby("Team")["Win"]
               .sum()
               .reset_index()
               .sort_values(by="Win", ascending=False)
               .head(5))

#Golos Totais por jogo - HISTOGRAMA
df_jogo = df.iloc[1:].copy()

df_jogo["Total_Golos"] = df_jogo["FTHG"] + df_jogo["FTAG"]













# --- CONFIGURAÇÃO DO DASHBOARD ---
# Criamos uma figura e uma matriz de eixos (2 linhas e 2 colunas)
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 12))
fig.suptitle('Premier League Dashboard - Season Analysis', fontsize=20, fontweight='bold', y=0.95)

# Dica: 'axes' é uma matriz 2x2. Para facilitar, podemos achatar para axes[0], axes[1]...
ax = axes.flatten()

# --- GRÁFICO 1: TOP 5 VITÓRIAS (Seu gráfico atual) ---
bars1 = ax[0].barh(top_5_wins["Team"][::-1], top_5_wins["Win"][::-1], color='lightgreen')
ax[0].set_title("TOP 5 Teams - Total Wins", fontsize=14, pad=10)
ax[0].set_xlabel("Wins")
ax[0].bar_label(bars1, padding=5, fontweight='bold')
ax[0].grid(axis='x', linestyle='--', alpha=0.6)

# --- GRÁFICO 2: ESPAÇO PARA O PRÓXIMO (Ex: Gols ou Cartões) ---
bins = range(0, df_jogo['Total_Golos'].max() + 2) 
ax[1].hist(df_jogo['Total_Golos'], bins=bins, color='skyblue', edgecolor='black', align='left')
ax[1].set_title("Distribution of Total Goals per Match", fontsize=14, pad=10)
ax[1].set_xlabel("Goals in a Single Match")
ax[1].set_ylabel("Number of Matches (Frequency)")
ax[1].set_xticks(range(0, df_jogo['Total_Golos'].max() + 1)) # Garante que todos os números apareçam no eixo X
ax[1].grid(axis='y', linestyle='--', alpha=0.4)


# --- GRÁFICO 3: ESPAÇO PARA O PRÓXIMO ---
ax[2].text(0.5, 0.5, 'Próxima Estatística\n(ex: Cartões Amarelos)', ha='center', va='center', fontsize=12, color='gray')
ax[2].set_title("Placeholder Estatística 3")

# --- GRÁFICO 4: ESPAÇO PARA O PRÓXIMO ---
ax[3].text(0.5, 0.5, 'Próxima Estatística\n(ex: Posse de Bola)', ha='center', va='center', fontsize=12, color='gray')
ax[3].set_title("Placeholder Estatística 4")

# Ajustar o layout para evitar sobreposição
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()