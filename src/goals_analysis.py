import pandas as pd

df = pd.read_csv("data/premier_league.csv")




#Média de golos por jogo
media = df[['FTHG', 'FTAG']].mean()

media_home = media['FTHG']
media_away = media['FTAG']
media_jogo = media.sum()

df = df.assign(Total_Goals = df['FTHG'] + df['FTAG'])


#Jogo com mais golos

max_golos = df[['FTHG', 'FTAG']].max().max()
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
print(f"Média de golos por jogo: {media_jogo:.2f}")

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