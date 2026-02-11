import pandas as pd

df = pd.read_csv("data/premier_league.csv")





#Criar coluna TotalGoals
df['TotalGoals'] = df['FTHG'] + df['FTAG']

#Média de golos por jogo
media_golos_jogo = df["TotalGoals"].mean()

#Média de golos por equipa
media_golos_equipa_casa = df.groupby("HomeTeam")['FTHG'].mean()
media_golos_equipa_fora = df.groupby("AwayTeam")['FTAG'].mean()







#Jogo com mais golos
jogo_max = df.loc[(df['FTHG'] + df['FTAG']).idxmax()]


#TOP5 Equipas que mais marcaram em casa

top5_home_goals = (
    df.groupby("HomeTeam")["FTHG"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

#TOP5 Equipas que mais sofreram fora
top5_away_against = (
    df.groupby("AwayTeam")["FTHG"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)


#PRINTS


print("=== GOAL ANALYSIS ===")

#MÉDIA GOLOS POR JOGO
print(f"Média de golos por jogo: {media_golos_jogo:.2f}")
print("\n" + "-"*30 + "\n")

#JOGO COM MAIS GOLOS
print("\nJogo com mais golos:")
print(f"Data: {jogo_max['Date']}")
print(f"Casa: {jogo_max['HomeTeam']} - Fora: {jogo_max['AwayTeam']}")
print(f"Resultado: {jogo_max['FTHG']}-{jogo_max['FTAG']}")

print("\n" + "-"*30 + "\n")

#TOP 5 GOLOS EM CASA
print("Top 5 equipas - Golos em Casa:")
for i, (equipa, golos) in enumerate(top5_home_goals.items(), 1):
    print(f"{i}. {equipa}: {golos}")
print("\n" + "-"*30 + "\n")

#TOP 5 SOFRIDOS FORA
print("Top 5 equipas - Golos Sofridos Fora:")
for i, (equipa, golos) in enumerate(top5_away_against.items(), 1):
    print(f"{i}. {equipa}: {golos}")