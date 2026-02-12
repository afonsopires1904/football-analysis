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


#A equipa com mais remates ganha quanta % dos jogos?

#Preciso de saber em cada jogo quem é que teve mais remates
df_analise = df.copy()

df_analise["MaisRemates"] = None

#Quantos jogos foram ganhos pela equipa que teve mais remates
for index, row in df_analise.iterrows():

    remates_casa = row["HS"]
    remates_fora = row["AS"]

    #comparar

    if remates_casa > remates_fora:
        df_analise.loc[index, "MaisRemates"] = "H"
    elif remates_casa < remates_fora:
        df_analise.loc[index, "MaisRemates"] = "A"
    else:
        df_analise.loc[index, "MaisRemates"] = "D"


df_analise["Ganhou_Remates"] = df_analise["MaisRemates"] == df_analise["FTR"]

# Fazer a percentagem
vitorias_mais_remates = df_analise['Ganhou_Remates'].sum()
derrotas_mais_remates = len(df_analise) - vitorias_mais_remates
percentagem = (vitorias_mais_remates / len(df_analise)) * 100

#% de equipas que ganham quando estão a ganhar ao intervalo

df_ht_win = df[df["HTR"] != "D"].copy()

df_ht_win["WinAtHT"] = None


for index, row in df_ht_win.iterrows():

    ht_result = row["HTR"]
    ft_result = row["FTR"]

    #comparar W - Win / NW - Not Win
    if ht_result == ft_result:
        df_ht_win.loc[index, "WinAtHT"] = "W"
    elif ht_result != ft_result:
        df_ht_win.loc[index, "WinAtHT"] = "NW"




#print(df_ht_win[['HomeTeam', 'AwayTeam', 'HTR', 'FTR', 'WinAtHT']].head(25))

total_ht = len(df_ht_win)
won = len(df_ht_win[df_ht_win['WinAtHT'] == 'W'])
did_not_win = len(df_ht_win) - won
percentagem_ht = (won / total_ht) * 100











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

# --- GRÁFICO 2: TOTAL GOLOS POR JOGO) ---
bins = range(0, df_jogo['Total_Golos'].max() + 2) 
ax[1].hist(df_jogo['Total_Golos'], bins=bins, color='skyblue', edgecolor='black', align='left')
ax[1].set_title("Distribution of Total Goals per Match", fontsize=14, pad=10)
ax[1].set_xlabel("Goals in a Single Match")
ax[1].set_ylabel("Number of Matches (Frequency)")
ax[1].set_xticks(range(0, df_jogo['Total_Golos'].max() + 1)) # Garante que todos os números apareçam no eixo X
ax[1].grid(axis='y', linestyle='--', alpha=0.4)

# --- GRÁFICO 3: EQUIPA COM MAIS REMATES GANHA? ---



# Dados para o gráfico
labels = ['Team with\n the most shots', 'Team with the\n most shots lost/draw']
sizes = [vitorias_mais_remates, derrotas_mais_remates]
colors = ["#37F637", "#F22020"]  # Verde claro, rosa claro
explode = (0.05, 0)  # "Explodir" a primeira fatia

# Criar pie chart
wedges, texts, autotexts = ax[2].pie(
    sizes, 
    labels=labels, 
    colors=colors,
    autopct='%1.1f%%',  # Mostrar percentagem
    explode=explode,
    startangle=90,
    textprops={'fontsize': 11, 'weight': 'bold'}
)

# Adicionar legenda com número de jogos
ax[2].legend(
    [f'Won: {vitorias_mais_remates} games', 
     f'Did not win: {derrotas_mais_remates} games'],
    loc='lower left',
    fontsize=10
)

ax[2].set_title(f"Does Team with More Shots Win?\n({percentagem:.1f}% of matches)", 
                fontsize=14, pad=10, weight='bold')

# --- GRÁFICO 4: % EQUIPAS QUE GANHAM QUANDO ESTÃO A GANHAR AO INTERVALO ---

# Dados para o gráfico
labels = ['Team winning at \n HT wins', 'Team winning at the\n HT does not win']
sizes = [won, did_not_win]
colors = ["#37F637", "#F22020"]  # Verde claro, rosa claro
explode = (0.05, 0)  # "Explodir" a primeira fatia

# Criar pie chart
wedges, texts, autotexts = ax[3].pie(
    sizes, 
    labels=labels, 
    colors=colors,
    autopct='%1.1f%%',  # Mostrar percentagem
    explode=explode,
    startangle=90,
    textprops={'fontsize': 11, 'weight': 'bold'}
)

# Adicionar legenda com número de jogos
ax[3].legend(
    [f'Won: {won} games', 
     f'Did not win: {did_not_win} games'],
    loc='lower left',
    fontsize=10
)
ax[3].set_title(f"Teams Leading at Half-Time\n({percentagem_ht:.1f}% maintain lead)", 
                fontsize=14, pad=10, weight='bold')

# Ajustar o layout para evitar sobreposição
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('outputs/graph/dashboard.png', dpi=300, bbox_inches='tight')
print("✅ Dashboard stored: outputs/graph/dashboard.png")
plt.show()