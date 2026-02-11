import pandas as pd



df = pd.read_csv("data/premier_league.csv")

print("=== DATASET EXPLORE ===")

#Primeiras 5 linhas
print("First 5 rows:", df.head())
print("\n" + "="*50 + "\n")

#Info sobre colunas
print("Column information:", df.info(97))
print("\n" + "="*50 + "\n")

#Estatisticas Descritivas
print("Descriptive statistics:", df.describe())
print("\n" + "="*50 + "\n")

#Equipas
equipas = df["HomeTeam"].unique()
print("Equipas:", equipas)
print("\n" + "="*50 + "\n")

#==========#=========#

#Quantos jogos existem no dataset?
# 380
print(f"Total de jogos no data set: {df.shape[0]}")
print("\n" + "="*50 + "\n")

#Quantas colunas existem?
# 106
print(f"Total de colunas: {df.shape[1]}")
print("\n" + "="*50 + "\n")

#Que colunas têm dados sobre golos?
# 4 - FTHG, FTAG, HTHG, HTAG
gol_columns = [col for col in df.columns if 'G' in col]
print(f"Colunas sobre golos: {gol_columns}")
print("\n" + "="*50 + "\n")

#Existem valores nulos (NAN)?
# Sim
total_nulos = df.isnull().sum().sum()
print(f"Valores nulos: {total_nulos}")
print("\n" + "="*50 + "\n")
      
#Quantas equipas existem no dataset?
# 20 equipas
num_equipas = df["HomeTeam"].nunique()
print(f"Número de equipas: {num_equipas}")
print("\n" + "="*50 + "\n")